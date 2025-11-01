# 🛡️ Network Intrusion Detection System (NIDS) using Machine Learning

📅 **Project Duration:** 26 June 2023 – 06 September 2023 (2 Months 10 days)  
🎓 **Academic Level:** MSc Information Security & Digital Forensics  
🏫 **Institution:** University of East London, London, UK  
👨‍🏫 **Supervisor:** Dr. Ameer Al-Nemrat  

This repository contains an academic project demonstrating a **Machine Learning-based Network Intrusion Detection System (NIDS)** using the **KDD Cup 1999 dataset**. The project includes preprocessing, model training, evaluation, and visualization of multiple ML classifiers.

---

## 🏫 Project Overview

Network security is a crucial aspect of cybersecurity, and **Intrusion Detection Systems (IDS)** play a key role in monitoring network traffic for suspicious activity. This project implements a **data-driven IDS** using machine learning, allowing for the detection of network intrusions based on historical data.

**Key Features:**
- Handles both binary classification (normal vs attack) and multi-class attack detection.
- Preprocessing pipeline includes encoding, scaling, and balancing (SMOTE) of imbalanced datasets.
- Supports multiple classifiers: **GaussianNB, RandomForest, KNN, SVC, and AdaBoost**.
- Generates performance metrics: accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrices.
- Provides visual comparisons of model performance.

---

## 🎯 Project Objectives

- Build a reliable ML-based IDS for detecting network intrusions.
- Compare the performance of multiple classifiers on imbalanced datasets.
- Provide a reproducible pipeline for preprocessing, training, evaluation, and visualization.
- Highlight the application of ML techniques in cybersecurity research.
- Create an academic reference project demonstrating ML for intrusion detection.

---

## ⚙️ Methodology & Roadmap

**Project Workflow:**
1. **Load Dataset**: Import `KDDTrain+.txt` and `KDDTest+.txt`.
2. **Preprocessing**:
   - Encode categorical features.
   - Scale numerical features using MinMaxScaler.
   - Balance the dataset using SMOTE.
3. **Train Models**:
   - GaussianNB, RandomForest, KNN, SVC, AdaBoost.
4. **Evaluate Models**:
   - Calculate accuracy, precision, recall, F1-score, ROC-AUC.
   - Generate confusion matrices.
5. **Visualization**:
   - Compare metrics and confusion matrices visually.
   - Save results to `results/` folder for academic analysis.

**Framework:**
- Python 3.11
- Libraries: pandas, numpy, scikit-learn, imbalanced-learn, seaborn, matplotlib, joblib

## 📊 Key Performance Indicators (KPIs)

| Model         | Accuracy | Precision | Recall  | F1-Score | ROC-AUC |
|---------------|---------|----------|--------|----------|---------|
| AdaBoost      | 1.000   | 1.000    | 1.000  | 1.000    | 1.000   |
| GaussianNB    | 0.997   | 0.995    | 0.999  | 0.997    | 0.996   |
| RandomForest  | 0.952   | 0.982    | 0.933  | 0.957    | 0.955   |
| SVC           | 0.844   | 0.932    | 0.782  | 0.851    | 0.853   |
| KNN           | 0.810   | 0.932    | 0.719  | 0.812    | 0.825   |

**KPI Roadmap:**
- **High Accuracy & Recall:** Ensure minimal false negatives for intrusions.
- **Precision & F1-Score:** Balance detection quality across classes.
- **ROC-AUC:** Assess overall classifier performance.
- **Visualization:** Compare metrics and confusion matrices to select the best model (AdaBoost).

---

## 🌟 Advantages

✅ Accurate intrusion detection with AdaBoost achieving perfect scores.  
✅ Modular, reproducible ML pipeline.  
✅ Visualization of model comparisons for academic reporting.  
✅ Can serve as a reference for research or academic studies.  
✅ Dataset-independent preprocessing pipeline – reusable with other datasets.  

---

## ⚠️ Limitations

| Limitation                     | Description                              | Possible Improvement                     |
|--------------------------------|------------------------------------------|-----------------------------------------|
| Academic Dataset Only           | Uses KDD 1999 dataset, not real-time data| Integrate real network traffic for testing |
| Binary & Limited Multi-class    | Some attacks may not be represented well | Use updated intrusion datasets (NSL-KDD, CICIDS2017) |
| No Deployment Pipeline          | Not connected to live IDS environment    | Implement real-time network packet capture and analysis |
| Resource Heavy Models           | RandomForest & AdaBoost require more compute | Optimize models or use lighter classifiers |

---

## 🔮 Future Scope

- Adapt system for **real-time intrusion detection**.  
- Integrate **modern datasets** for broader attack coverage.  
- Deploy as a cloud-based IDS dashboard with **live monitoring**.  
- Implement **automated alerts and reports** for network admins.  
- Explore **deep learning approaches** for anomaly detection.  

---

## ⏱️ Academic Project Timeline

| Stage                         | Start Date   | End Date     | Notes                                      |
|-------------------------------|------------|------------|--------------------------------------------|
| Introduction                  | 26-06-2023 | 19-07-2023 | Project overview, motivation, challenges  |
| Literature Review             | 30-06-2023 | 25-07-2023 | IDS research, NIDS methods, research gaps|
| Research Methodology          | 02-07-2023 | 30-07-2023 | Methodology, flowcharts, algorithms      |
| Experimental Results          | 28-07-2023 | 19-08-2023 | Dataset processing, training, testing    |
| Analysis & Result Discussion  | 10-08-2023 | 05-09-2023 | Evaluation metrics, model comparison     |
| Conclusion & Future Directions | 01-09-2023 | 05-09-2023 | Research findings, future scope          |
| Final Submission              | 06-09-2023 | 07-09-2023 | Complete project report                   |

---

## 🧩 Features Summary

| Feature                        | Description |
|--------------------------------|------------|
| Dataset Handling                | Load, encode, scale, and balance network data |
| Model Training                  | Train multiple ML classifiers with hyperparameters |
| Evaluation Metrics              | Accuracy, precision, recall, F1, ROC-AUC, confusion matrices |
| Visualization                   | Save comparison charts in `results/figures/compare/` |
| Pre-trained Models              | Save and load models using `.joblib` files |
| Modular Scripts                 | `src/` contains all preprocessing, training, evaluation, and visualization scripts |

---

## 💻 Technologies Used

| Category       | Tools                                      |
|----------------|--------------------------------------------|
| Programming    | Python 3.11                                |
| Data Handling  | pandas, numpy                              |
| ML Libraries   | scikit-learn, imbalanced-learn             |
| Visualization  | matplotlib, seaborn                        |
| Persistence    | joblib                                     |
| Version Control| Git & GitHub                               |

---

## 📝 Modernisation Note

- **Originally built:** 26 June – 06 September 2023 (Academic project)  
- **Uploaded & documented for GitHub:** October 2025  
- **Modern updates & improvements for public sharing:**  
  - Cleaned project files for clarity and reproducibility.  
  - Added modular Python scripts (`src/`) for preprocessing, training, evaluation, and visualization.  
  - Included pre-trained model `.joblib` files.  
  - Organized results into `results/` for metrics, figures, and comparisons.  
  - Compatible with Python 3.11 and latest libraries.  

## 📜 Disclaimer

- This project was developed purely as an academic exercise as part of MSc coursework in Information Security & Digital Forensics.  
- The dataset used (KDD Cup 1999) is outdated and for educational purposes only.  
- Results are illustrative and may not reflect real-world network behavior.  
- This project does not provide any guarantee of accuracy, security, or reliability for operational or production systems.  
- Users and researchers are responsible for verifying and adapting methods before applying in real environments.  

⚠️ **The purpose of this repository is to demonstrate machine learning techniques for intrusion detection in an academic context only.**

## 🧩 Conclusion

- The Network Intrusion Detection System (NIDS) demonstrates the application of machine learning in cybersecurity.  
- AdaBoost achieved perfect scores on the dataset.  
- Provides a complete pipeline: preprocessing, training, evaluation, visualization.  
- Supports academic analysis and comparison of ML classifiers.  
- Serves as a foundation for future real-time intrusion detection systems.



## ⚡ Quick Setup Guide
---

## 🛡️ Large File Handling (Git LFS)

Some project files (datasets and trained ML models) are **larger than GitHub’s 100 MB limit**, so they are tracked using **Git Large File Storage (LFS)**.  

**Steps to clone and get all files:**

```bash
# Install Git LFS (if not already installed)
git lfs install

# Clone repository
1️⃣ git clone https://github.com/AnilkumarDave/Network-Intrusion-Detection-System_ML.git

# Pull LFS-tracked files
git lfs pull

cd network-intrusion-ml

2️⃣ Create a virtual environment and install dependencies

python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

3️⃣ Run Jupyter Notebook

jupyter notebook network_intrusion_detection.ipynb

4️⃣ Results

Models, metrics, and visualizations will be saved automatically in results/.

Tracked large files:

results/processed_train.csv

results/processed_test.csv

results/models/*.joblib


✨ Author

Name: Anilkumar Dave
Email: daveanil48@gmail.com
