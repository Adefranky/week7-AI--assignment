Q1: Define algorithmic bias and provide two examples of how it manifests in AI systems.
Algorithmic bias is the systematic and unfair discrimination in AI systems caused by biased data, flawed assumptions, or model design choices. It leads to outcomes that favor or disadvantage certain groups.
Examples:
1.	Biased facial recognition
AI systems misidentify people with darker skin tones more frequently because they were trained predominantly on lighter-skinned faces.
2.	Discriminatory hiring algorithms
Recruitment AI may downgrade applications from women if historical data reflects male-dominated hiring patterns, causing the model to learn biased associations.
Q2: Explain the difference between transparency and explainability in AI. Why are both important?
•	Transparency refers to how open and observable an AI system is—its data sources, model architecture, training process, and how decisions are made.
•	Explainability is the ability of the AI system to provide understandable reasons for its decisions in a human-interpretable way.
Why both matter:
•	Transparency builds trust by showing how the system was created and what data it uses.
•	Explainability supports accountability, enabling users and regulators to understand and challenge decisions.
•	Together, they improve ethical use, reduce harm, and help meet legal or compliance requirements.
Q3: How does GDPR (General Data Protection Regulation) impact AI development in the EU?
GDPR impacts AI development in several key ways:
1.	Data protection and consent:
AI developers must obtain explicit, lawful consent before collecting or processing personal data.
2.	Right to explanation:
Users can request meaningful explanations for automated decisions that significantly affect them, pushing AI systems toward explainability.
3.	Data minimization:
Only necessary data can be collected, limiting how much information AI systems can use.
4.	Accountability and penalties:
Organizations must document AI processes and ensure compliance, with heavy fines for violations.
Overall, GDPR ensures AI systems are ethical, transparent, privacy-preserving, and user-centric.
2
A) Justice → Fair distribution of AI benefits and risks.
B) Non-maleficence → Ensuring AI does not harm individuals or society.
C) Autonomy → Respecting users’ right to control their data and decisions.
D) Sustainability → Designing AI to be environmentally friendly.

Case 1: Biased Hiring Tool – Amazon Example
1. Identify the Source of Bias
Amazon’s AI recruiting tool became biased mainly due to:
a) Biased training data
The model was trained on 10 years of resumes, most of which came from men because the tech industry historically hires more men.
→ The model learned that “male-dominated patterns” = successful candidates.
b) Feature associations learned by the model
The AI penalized words like “women’s chess club captain” because it associated anything linked to women with lower hiring success.
c) Lack of fairness constraints in model design
The algorithm was optimized for predicting past hiring decisions, not for ensuring fairness or equal opportunity.
2. Propose Three Fixes to Make the Tool Fairer
Fix 1: Debias the training data
•	Rebalance the dataset to include equal representation of male and female candidates.
•	Remove gender-correlated features (e.g., terms that imply gender).
Fix 2: Add fairness constraints to the model
•	Use algorithms such as Equalized Odds, Demographic Parity, or Counterfactual Fairness.
•	Ensure the model cannot rely on gender-related features, even indirectly.
Fix 3: Human-AI hybrid decision-making
•	Use AI to assist but not fully automate hiring.
•	Include human review, especially when the AI flags or downranks a candidate.
(Optional additional fix if allowed: Continuous fairness auditing using bias detection tools like IBM AI Fairness 360.)
3. Suggest Metrics to Evaluate Fairness Post-Correction
Use measurable fairness metrics to check improvements:
a) Demographic Parity
The percentage of female and male candidates recommended by the AI should be similar.
b) Equal Opportunity / Equalized Odds
The AI should have equal:
•	True positive rates (qualified candidates selected)
•	False negative rates (qualified candidates rejected)
across gender groups.
c) Disparate Impact Ratio
The hiring recommendation rate for women should be at least 80% of that for men
(the “80% rule” used in fairness evaluation).
Case 2: Facial Recognition in Policing
1. Ethical Risks
a) Wrongful arrests and discrimination
Facial recognition systems often misidentify Black, Asian, and minority ethnic groups at higher rates.
This can lead to:
•	Wrongful arrests
•	Unjust surveillance
•	Reinforcement of racial profiling in policing
b) Violation of privacy and civil liberties
Facial recognition captures biometric data without explicit consent.
Risks include:
•	Mass surveillance
•	Tracking people’s movements
•	Loss of anonymity in public spaces
c) Lack of transparency and accountability
Police may rely heavily on the system without understanding how it works.
This leads to:
•	Opaque decision-making
•	Difficulty proving when or how errors occurred
•	Reduced trust between communities and law enforcement
d) Erosion of public trust
Communities—especially minorities—may feel targeted, worsening police–community relations and creating fear of public spaces.
2. Policies for Responsible Deployment
Policy 1: Mandatory accuracy and bias testing before use
Systems must undergo:
•	Independent audits
•	Benchmarking on diverse demographic datasets
•	Annual bias evaluations
→ Only systems meeting fairness standards should be approved.
Policy 2: Strict regulations on when the technology can be used
Usage should be limited to:
•	High-risk criminal investigations
•	Cases with judicial warrants
•	Situations where human review is mandatory
→ No deployment for general public surveillance.
Policy 3: Human-in-the-loop verification
Facial recognition matches must never be treated as proof.
Police officers must:
•	Verify all matches manually
•	Use multiple pieces of evidence before taking action
Policy 4: Data protection and privacy safeguards
Implement:
•	Explicit consent for data collection where applicable
•	Limits on retention of biometric data
•	Secure storage and access controls
Policy 5: Transparency and public reporting
Require:
•	Public documentation of system performance
•	Community consultations before deployment
•	Clear logs of when and why the system was used
Policy 6: Accountability and legal remedies
If wrongful identification occurs:
•	Individuals should have the right to review and challenge the technology’s output
•	Agencies must be legally liable for misuse or negligence
•	300-word Audit Report (copy/paste)
•	COMPAS dataset audit — summary & remediation (300 words)
•	An audit of the COMPAS recidivism dataset examined predictive risk scores across racial groups to evaluate disparities. Using the dataset’s predicted risk (decile score → binary prediction) and the two-year recidivism outcome, group-level metrics were calculated: predicted positive rate (how often the model flags someone as high risk), false positive rate (FPR), and true positive rate (TPR). Visualizations of FPR and TPR by race were produced to highlight relative differences.
•	The analysis typically reveals that racial minorities, particularly African-American and other underrepresented groups, experience higher FPRs compared to Whites: they are more likely to be incorrectly flagged as high risk when they do not re-offend. TPRs vary, but disparities in TPR or FPR indicate the model does not treat demographic groups equally — creating risk of discriminatory outcomes such as unfair sentencing recommendations. These patterns point to biases originating primarily from historical data and label bias (systemic differences in arrest, charging, or sentencing practices), and possibly feature choice and model optimization that prioritize overall accuracy over equitable error rates.
•	Recommended remediation steps include (1) data-level interventions: reweight or resample training data to correct representation imbalances and remove proxy features that encode protected information; (2) in-model fairness constraints: apply fairness-aware learning (e.g., Equalized Odds, adversarial debiasing) to reduce differences in FPR/TPR across groups while monitoring utility; and (3) post-processing: calibrate thresholds per group or use equalized odds postprocessing to adjust decisions while preserving overall performance. Operational safeguards are also necessary: require human review for flagged individuals, log and publicly report system performance by group, limit use to contexts with legal oversight, and conduct regular audits. Evaluation should track multiple fairness metrics (demographic parity, equalized odds, disparate impact) and ensure remediation does not produce new harms.

•	Part 4: Ethical Reflection 
•	In my future projects—particularly those involving data-driven decision systems such as the animal tracking system or any predictive model I may build—I will prioritize ethical AI principles from the design stage through deployment. To ensure fairness, I will carefully examine the data sources, check for imbalance, and apply preprocessing techniques that minimize bias. I will test the model on diverse user groups to ensure that no community is disadvantaged by the system’s outputs.
•	To uphold transparency and explainability, I will document model choices, data assumptions, and decision logic. Wherever possible, I will implement interpretable models or provide explanation tools so that users can understand how predictions are generated. This also supports accountability in case the system behaves incorrectly.
•	I will actively ensure privacy and data protection by collecting only essential data and applying techniques such as encryption, anonymization, and secure storage. For user-facing systems, I will obtain informed consent and give users control over how their data is used.
•	In applying non-maleficence, I will assess potential harms early—such as misuse of location data or misclassification risks—and put safeguards in place. This includes rate limiting, access control, and constant model monitoring to detect and correct unexpected behavior.
•	Lastly, I will consider sustainability, ensuring that the system is computationally efficient and mindful of energy consumption. By incorporating explainability, fairness audits, secure data practices, and responsible deployment, I will ensure that my project aligns with ethical AI principles and contributes positively to users and society.

Policy Proposal: Ethical AI Use in Healthcare
(1-Page Guideline)
1. Introduction
This policy provides guidelines to ensure the ethical development, deployment, and use of Artificial Intelligence (AI) systems in healthcare settings. It aims to safeguard patient rights, promote fairness, ensure transparency, and protect public trust. These guidelines apply to all stakeholders, including healthcare providers, AI developers, administrators, and third-party vendors.
2. Patient Consent Protocols
1.	Informed Consent Before Data Use
o	Healthcare institutions must obtain explicit, written or digital consent from patients before collecting, storing, or using their medical data for AI training, prediction, or analysis.
o	Consent forms must clearly state:
	What data is being used
	Why the data is needed
	How the AI system will operate
	Any potential risks or limitations
2.	Right to Opt-Out
o	Patients must be allowed to decline AI involvement in their care without facing discrimination or denial of service.
3.	Data Anonymization and Minimization
o	Only the minimum necessary data should be collected.
o	Data must be de-identified whenever possible to protect patient identity.
4.	Secondary Use of Data
o	If patient data will be reused for research, model retraining, or shared across institutions, additional consent must be requested.
3. Bias Mitigation Strategies
1.	Diverse and Representative Datasets
o	AI developers must ensure datasets include diverse demographics (age, gender, ethnicity, geography) to reduce algorithmic bias.
o	Underrepresented groups must be deliberately included in model training.
2.	Regular Fairness Audits
o	AI systems must be audited quarterly or annually to detect disparities in outcomes across patient groups.
o	Audits should measure accuracy, false-positive rates, false-negative rates, and treatment recommendations across demographic groups.
3.	Bias Reporting Mechanism
o	Healthcare workers must have a clear channel to report suspected bias or unfair outcomes generated by the AI system.
4.	Human Oversight
o	Final clinical decisions must remain under the responsibility of licensed healthcare professionals who can override AI recommendations.
4. Transparency Requirements
1.	Explainability of AI Decisions
o	AI systems used for diagnosis or treatment recommendations must provide explainable outputs so that clinicians and patients can understand the reasoning behind predictions.
2.	Disclosure to Patients
o	Patients must be informed whenever AI tools are used in diagnosis, prognosis, or treatment planning.
o	Communication should use clear, non-technical language.
3.	Model Documentation
o	Developers must provide detailed documentation including:
	Data sources
	Model assumptions
	Known limitations
	Performance metrics
	Appropriate use cases
4.	Incident Reporting
o	Any AI malfunction, misdiagnosis, or harmful suggestion must be immediately documented and reported to regulatory oversight bodies.
5. Data Security and Privacy Protection
1.	Compliance with Regulations
o	All AI systems must comply with local data protection laws (e.g., GDPR, HIPAA-equivalent frameworks).
2.	Encryption and Access Control
o	Patient data must be encrypted both in transit and at rest.
o	Access must be restricted to authorized personnel only.
3.	Data Retention Policy
o	Data should be stored only for as long as necessary and deleted securely afterward.
6. Accountability and Governance
1.	Clear Roles and Responsibilities
o	Each healthcare organization must define who is responsible for model monitoring, data security, maintenance, and ethical oversight.
2.	Ethics Review Board
o	An independent committee should review all healthcare AI systems before deployment.
3.	Continuous Monitoring
o	AI tools must be continuously evaluated for accuracy, performance drift, and unintended consequences.
7. Conclusion
Implementing ethical AI in healthcare requires a commitment to fairness, transparency, patient autonomy, and rigorous governance. By following these guidelines, institutions can ensure responsible and trustworthy AI deployment that prioritizes patient welfare and enhances clinical outcomes.

