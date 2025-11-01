#!/usr/bin/env python3
"""
visualize.py
Load saved models and processed test set, plot confusion matrices and ROC curves.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import confusion_matrix, roc_curve, auc

# Paths
TEST_CSV = "results/processed_test.csv"
MODEL_DIR = "results/models"
FIG_DIR = "results/figures"
os.makedirs(FIG_DIR, exist_ok=True)

# Load test data
df_test = pd.read_csv(TEST_CSV)

# Identify numeric features
cols_to_drop = ['binary_label', 'orig_label']
existing_cols_to_drop = [c for c in cols_to_drop if c in df_test.columns]

feature_cols = [c for c in df_test.columns 
                if c not in existing_cols_to_drop 
                and df_test[c].dtype != 'object']

X_test = df_test[feature_cols].values
y_test = df_test['binary_label'].values

# Load all models in MODEL_DIR
models = {}
for file in os.listdir(MODEL_DIR):
    if file.endswith(".joblib"):
        model_name = file.replace(".joblib", "")
        models[model_name] = joblib.load(os.path.join(MODEL_DIR, file))

# Plot settings
sns.set(style="whitegrid")

for name, model in models.items():
    print(f"Visualizing {name} ...")
    # Predictions
    y_pred = model.predict(X_test)
    try:
        y_proba = model.predict_proba(X_test)[:,1]
    except AttributeError:
        y_proba = None

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, f"{name}_confusion_matrix.png"))
    plt.close()

    # ROC curve
    if y_proba is not None:
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = auc(fpr, tpr)
        plt.figure(figsize=(5,4))
        plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
        plt.plot([0,1],[0,1],'k--')
        plt.title(f"{name} ROC Curve")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.legend(loc="lower right")
        plt.tight_layout()
        plt.savefig(os.path.join(FIG_DIR, f"{name}_roc_curve.png"))
        plt.close()

print("✅ Visualization complete! Figures saved in results/figures/")
