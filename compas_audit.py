"""
COMPAS fairness audit script
Saves:
 - fpr_by_race.png
 - tpr_by_race.png

Expect: compas.csv in working directory (ProPublica COMPAS).
This script does NOT require AIF360, but has an optional block to use it.
"""
import os
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# -------------------------
# Load dataset
# -------------------------
FNAME = "compas.csv"
if not os.path.exists(FNAME):
    raise FileNotFoundError(
        f"{FNAME} not found. Download the ProPublica COMPAS dataset and save as {FNAME}."
    )

df = pd.read_csv(FNAME)

# The ProPublica COMPAS data uses columns like:
# 'age', 'sex', 'race', 'score_text' or 'decile_score', 'two_year_recid'
# If your CSV has different column names, adapt below.

# Basic expected columns (try several common names)
if 'two_year_recid' not in df.columns:
    # attempt to infer
    possible = [c for c in df.columns if 'two' in c and 'recid' in c]
    if possible:
        df.rename(columns={possible[0]:'two_year_recid'}, inplace=True)
    else:
        raise KeyError("Can't find 'two_year_recid' column. Please supply COMPAS data.")

if 'race' not in df.columns:
    raise KeyError("Can't find 'race' column in dataset.")

# Predicted risk: some versions have 'score_text' (Low/Medium/High) or 'decile_score'
# We'll construct a binary predicted label 'pred_label' using decile_score >= 5 or score_text.
if 'decile_score' in df.columns:
    df['pred_label'] = (df['decile_score'] >= 5).astype(int)
elif 'score_text' in df.columns:
    df['pred_label'] = df['score_text'].apply(lambda s: 1 if str(s).lower() in ['medium', 'high'] else 0)
else:
    # fallback: if there's a model predicted probability column 'predicted' or 'risk_score'
    found = None
    for c in df.columns:
        if 'score' in c.lower() or 'risk' in c.lower() or 'pred' in c.lower():
            found = c
            break
    if found:
        df['pred_label'] = (df[found] >= df[found].median()).astype(int)
    else:
        raise KeyError("Can't find predicted risk/score column. Provide 'decile_score' or 'score_text' or similar.")

# True label
y_col = 'two_year_recid'
df = df[[ 'race', 'sex', y_col, 'pred_label']].dropna()
df.rename(columns={y_col:'y_true'}, inplace=True)

# Preprocess race groups: focus on major groups and an 'Other' bucket
race_counts = df['race'].value_counts()
major_races = race_counts.index[:6].tolist()  # top 6 races in dataset
df['race_grp'] = df['race'].apply(lambda r: r if r in major_races else 'Other')

# -------------------------
# Metrics by group
# -------------------------
def compute_confusion(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0,1]).ravel()
    return {'tn':tn,'fp':fp,'fn':fn,'tp':tp}

groups = df['race_grp'].unique().tolist()
metrics = {}
for g in groups:
    sub = df[df['race_grp']==g]
    c = compute_confusion(sub['y_true'], sub['pred_label'])
    # rates
    fpr = c['fp'] / (c['fp'] + c['tn']) if (c['fp'] + c['tn'])>0 else np.nan
    tpr = c['tp'] / (c['tp'] + c['fn']) if (c['tp'] + c['fn'])>0 else np.nan
    pp = sub['pred_label'].mean()  # predicted positive rate (demographic parity)
    metrics[g] = {'count': len(sub), 'fpr': fpr, 'tpr': tpr, 'pred_pos_rate': pp}

# Print table
print("Group | N | PredPosRate | FPR | TPR")
for g in sorted(metrics, key=lambda x: metrics[x]['count'], reverse=True):
    m = metrics[g]
    print(f"{g:12s} | {m['count']:4d} | {m['pred_pos_rate']:.3f} | {m['fpr']:.3f} | {m['tpr']:.3f}")

# -------------------------
# Plot FPR and TPR by race
# -------------------------
races = list(metrics.keys())
fprs = [metrics[r]['fpr'] for r in races]
tprs = [metrics[r]['tpr'] for r in races]
pred_rates = [metrics[r]['pred_pos_rate'] for r in races]

x = np.arange(len(races))
plt.figure(figsize=(10,5))
plt.bar(x, fprs)
plt.xticks(x, races, rotation=45, ha='right')
plt.ylabel("False Positive Rate")
plt.title("FPR by Race")
plt.tight_layout()
plt.savefig("fpr_by_race.png")
plt.close()

plt.figure(figsize=(10,5))
plt.bar(x, tprs)
plt.xticks(x, races, rotation=45, ha='right')
plt.ylabel("True Positive Rate")
plt.title("TPR by Race")
plt.tight_layout()
plt.savefig("tpr_by_race.png")
plt.close()

print("Saved fpr_by_race.png and tpr_by_race.png")

# -------------------------
# Optional: AIF360 usage (if installed)
# -------------------------
try:
    from aif360.datasets import BinaryLabelDataset
    from aif360.metrics import ClassificationMetric
    print("\nAIF360 detected. Building BinaryLabelDataset and showing example metrics...")
    bld = BinaryLabelDataset(df=df, label_names=['y_true'], protected_attribute_names=['race_grp'])
    # note: AIF360 expects pred_label as scores; we'll clone and add predictions
    bld_pred = bld.copy()
    bld_pred.labels = df['pred_label'].values.reshape(-1,1)
    cm = ClassificationMetric(bld, bld_pred, unprivileged_groups=[{'race_grp':'African-American'}], privileged_groups=[{'race_grp':'Caucasian'}])
    print("Disparate impact (pred):", cm.disparate_impact())
    print("False negative rate difference:", cm.false_negative_rate_difference())
except Exception as e:
    print("AIF360 not used (missing or failed). Error:", str(e))
    print("To use AIF360, install it and re-run the script.")
