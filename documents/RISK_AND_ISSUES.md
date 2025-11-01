# ⚠️ Risk & Issue Log — Network Intrusion Detection System (NIDS)

This log identifies potential risks and issues encountered during the Machine Learning-based NIDS project, along with their likelihood, impact, and mitigation measures.

| ID  | Risk / Issue | Category | Likelihood | Impact | Mitigation / Action | Status |
|-----|--------------|---------|------------|--------|-------------------|--------|
| R1  | Large dataset size causing slow training time | Technical | High | Medium | Used sampling, optimized data preprocessing, and reduced features during testing | ✅ Mitigated |
| R2  | Imbalanced dataset leading to biased model results | Data Quality | High | High | Applied SMOTE (Synthetic Minority Oversampling Technique) for balancing | ✅ Mitigated |
| R3  | Inconsistent categorical encoding between train and test sets | Technical | Medium | High | Ensured same encoder mapping for both sets and validated feature alignment | ✅ Mitigated |
| R4  | Model overfitting on training data | Model Performance | Medium | High | Used cross-validation and compared multiple models to ensure generalization | ✅ Mitigated |
| R5  | Misinterpretation of model accuracy as real-time security assurance | Compliance / Ethical | Medium | High | Added disclaimer in README.md — academic use only, not production-grade security system | ✅ Mitigated |
| R6  | Dependency version mismatch (e.g., scikit-learn updates) | Technical | Medium | Medium | Specified tested versions in requirements.txt for reproducibility | ✅ Mitigated |

> **Note:**  
All risks were actively monitored and mitigated during the project lifecycle through careful documentation, methodological rigor, and academic supervision.
