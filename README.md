# 🛡️ Network Intrusion Detection System (NIDS) using Machine Learning

📅 **Project Duration:** 26 June 2023 – 06 September 2023 (2 Months 10 days)  
🎓 **Academic Level:** MSc Information Security & Digital Forensics  
🏫 **Institution:** University of East London, London, UK  
👨‍🏫 **Supervisor:** Dr. Ameer Al-Nemrat  

This repository contains an academic project demonstrating a **Machine Learning-based Network Intrusion Detection System (NIDS)** using the **KDD Cup 1999 dataset**. The project includes preprocessing, model training, evaluation, and visualization of multiple ML classifiers.

---

## 🏫 Project Overview

Network security is a crucial aspect of cybersecurity, and **Intrusion Detection Systems (IDS)** play a key role in monitoring network traffic for suspicious activity. This project implements a **data-driven IDS** using machine learning, allowing for the detection of network intrusions based on historical data. he aim is to distinguish between normal traffic and
different categories of attacks (e.g. DoS, Probe, R2L, U2R).

**Key Features:**
- Data cleaning and feature engineering for NSL-KDD
- Training and comparison of multiple classifiers (e.g. Random Forest, Gradient Boosting)
- Evaluation using accuracy, precision, recall and F1-score
- Saving the best model for later prediction
- Providing a simple API layer so that other systems can query the trained model

---

## 🎯 Project Objectives

- Build a reproducible ML pipeline for network intrusion detection  
- Evaluate different algorithms and choose a suitable model  
- Expose the model via a small REST API for integration and testing  
- Demonstrate how security and networking projects can be combined with modern ML tooling  

---

📂 Project Structure (high level)

- `data/` – dataset files (not included in the repo if large)  
- `notebooks/` – Jupyter notebooks for exploration and model development  
- `src/` – Python modules for preprocessing, training and evaluation  
- `models/` – saved models (e.g. `best_model.pkl`)  
- `api/` – Flask app exposing the trained model via a REST API  
- `automation/` – Java RestAssured tests for the API  
- `README.md` – project documentation 

## 🌐 API Layer (`/api`)

The `/api` folder contains a small Flask application which:

- Loads the trained model (for example from `models/best_model.pkl`)  
- Exposes a `/predict` endpoint that accepts JSON with feature values  
- Returns a JSON response with fields such as `prediction` and `probabilities`  

See `api/README.md` for details.

## 🔧 API Test Automation (`/automation`)

The `/automation` folder contains a Java project that uses:

- **JUnit 5** for structuring tests  
- **RestAssured** for calling the `/predict` endpoint  
- **Maven** for dependency management and builds  

Example checks include:

- `/health` endpoint returns HTTP 200  
- `/predict` returns HTTP 200 for valid JSON input  
- Response body contains expected JSON fields  

See `automation/README.md` for more detail.

## 🚀 Quick Start (ML + API)

1. Train or load an existing model using the Python code/notebooks.  
2. Ensure the trained model is saved at the path expected by the Flask app,
   e.g. `models/best_model.pkl`.  
3. From the `api` folder, install dependencies and run the Flask app:

```bash
pip install -r requirements.txt
python app.py
```

4. The API will listen on `http://127.0.0.1:5000` by default.  
   - `GET /health` – simple health check  
   - `POST /predict` – send JSON with feature values to get a prediction  

## 🚦 Running API Tests (Java + RestAssured)

From the `automation` folder:

```bash
mvn clean test
```

This will run the JUnit tests against the running Flask API instance and
confirm that the key endpoints are behaving as expected.

## 🧪 CI Integration (Jenkins)

A simple `Jenkinsfile` at the root of the repository demonstrates how this
project can be used in a CI pipeline:

1. Check out the code  
2. Optionally start the Flask API (e.g. via a shell script)  
3. Run `mvn clean test` in the `/automation` folder  
4. Archive the JUnit test reports  

This shows how an ML-based security project can be exercised automatically
whenever changes are pushed.

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
