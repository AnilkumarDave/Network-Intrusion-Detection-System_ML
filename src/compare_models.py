#!/usr/bin/env python3
"""
compare_models.py
Compare trained models using metrics.csv and plot bar charts + ROC curves.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import roc_curve, auc

# Create results/figures/compare folder
os.makedirs("results/figures/compare", exist_ok=True)

# Load metrics
metrics_df = pd.read_csv("results/metrics.csv")
print("Metrics loaded:")
print(metrics_df)

# -----------------------------
# Step 1: Bar chart comparison
# -----------------------------
metrics_to_plot = ["accuracy", "precision", "recall", "f1", "roc_auc"]

for metric in metrics_to_plot:
    plt.figure(figsize=(8,5))
    plt.bar(metrics_df["model"], metrics_df[metric], color='skyblue')
    plt.title(f'Model Comparison - {metric.capitalize()}')
    plt.ylabel(metric.capitalize())
    plt.ylim(0,1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"results/figures/compare/{metric}_comparison.png")
    plt.close()
print("Bar charts saved in results/figures/compare/")

# -----------------------------
# Step 2: ROC curves comparison
# -----------------------------
# Load test data
df_test = pd.read_csv("results/processed_test.csv")
X_test = df_test.drop(columns=["binary_label", "orig_label"], errors='ignore').values
y_test = df_test["binary_label"].values

plt.figure(figsize=(8,6))

for model_name in metrics_df["model"]:
    model_path = f"results/models/{model_name}.joblib"
    model = joblib.load(model_path)
    try:
        y_prob = model.predict_proba(X_test)[:,1]
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f"{model_name} (AUC = {roc_auc:.2f})")
    except:
        print(f"{model_name} does not support predict_proba(), skipping ROC curve.")

plt.plot([0,1], [0,1], 'k--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("results/figures/compare/roc_comparison.png")
plt.close()
print("ROC curves saved in results/figures/compare/")
