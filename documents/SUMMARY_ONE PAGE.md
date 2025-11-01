# 🛡️ One-Page Summary — Network Intrusion Detection System (NIDS) using Machine Learning

**Student:** Anilkumar Dave  
**Course:** MSc Information Security and Digital Forensics  
**Institution:** University of East London  
**Supervisor:** Dr. Ameer Al-Nemrat  
**Project Duration:** 26 June 2023 – 06 September 2023  

---

## 🎯 Project Overview

This academic project demonstrates the design and implementation of a **Network Intrusion Detection System (NIDS)** using Machine Learning techniques. The system analyses network traffic to identify normal and malicious activity, based on the **KDD Cup 1999 dataset** — a benchmark dataset widely used in cybersecurity research.

**Objective:** Evaluate and compare multiple supervised ML algorithms for intrusion detection and determine the most effective model in terms of accuracy, recall, precision, and F1-score.

---

## ⚙️ Methodology

- **Dataset Preparation:** Loaded, cleaned, and normalized KDD Cup 1999 dataset.  
- **Pre-processing:** Encoded categorical attributes, scaled numeric values, and applied SMOTE for balancing.  
- **Model Training:** Implemented GaussianNB, Random Forest, KNN, SVC, and AdaBoost classifiers.  
- **Evaluation:** Measured accuracy, precision, recall, F1, and ROC-AUC.  
- **Visualization:** Generated performance charts and confusion matrices.

---

## 📊 Key Results

| Model       | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|------------|---------|-----------|-------|----------|---------|
| AdaBoost    | 1.000   | 1.000     | 1.000 | 1.000    | 1.000   |
| GaussianNB  | 0.997   | 0.995     | 0.999 | 0.997    | 0.996   |
| RandomForest| 0.952   | 0.982     | 0.933 | 0.957    | 0.955   |
| SVC         | 0.844   | 0.932     | 0.782 | 0.851    | 0.853   |
| KNN         | 0.810   | 0.932     | 0.719 | 0.812    | 0.825   |

**Note:** AdaBoost achieved perfect performance across all metrics, making it the most efficient algorithm for this dataset.

---

## ✅ Achievements & Advantages

- Modular ML pipeline for preprocessing, training, and evaluation.  
- Comparative analysis of multiple ML models.  
- Clear visual insights through performance charts.  
- High accuracy and recall, minimizing false negatives.  
- Reproducible academic project ready for research or real-time expansion.

---

## ⚠️ Limitations & Future Work

- Uses a static academic dataset; no live network traffic analysis.  
- Real-time implementation can use **NSL-KDD** or **CICIDS 2017** datasets.  
- Future work: real-time packet capture, deep learning models, dashboard-based monitoring.

---

## 🧩 Conclusion

This project demonstrates the power of machine learning in intrusion detection. Workflow, evaluation, and results provide a solid foundation for cybersecurity research and academic reference.

---

## 📜 Disclaimer

This project is for **educational purposes only**. Results are based on historical data and are not intended for live network protection without further adaptation.
