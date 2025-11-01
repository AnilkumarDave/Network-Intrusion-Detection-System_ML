#!/usr/bin/env python3
"""
evaluate.py
Load metrics and plot confusion matrix + ROC curves (if probabilities available).
"""
import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import roc_curve, auc, ConfusionMatrixDisplay
from sklearn.metrics import RocCurveDisplay

def plot_confusion_matrix(cm, model_name, out_path):
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix: {model_name}')
    plt.ylabel('True')
    plt.xlabel('Predicted')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main(args):
    os.makedirs("results/figures", exist_ok=True)
    metrics = pd.read_csv(args.metrics_csv)
    print(metrics[['model','accuracy','precision','recall','f1','roc_auc']])

    # For each model, load saved model and plot cm, and ROC if possible
    for idx, row in metrics.iterrows():
        model_name = row['model']
        model_path = f"results/models/{model_name}.joblib"
        if not os.path.exists(model_path):
            print("Model file not found:", model_path)
            continue
        model = joblib.load(model_path)
        # get confusion matrix saved in metrics file
        try:
            cm = eval(row['confusion_matrix']) if isinstance(row['confusion_matrix'], str) else row['confusion_matrix']
            cm = np.array(cm)
            plot_confusion_matrix(cm, model_name, f"results/figures/{model_name}_confusion.png")
            print("Saved confusion matrix for", model_name)
        except Exception as e:
            print("Could not plot confusion for", model_name, e)

    print("Evaluation figures saved to results/figures/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--metrics_csv", type=str, default="results/metrics.csv")
    args = parser.parse_args()
    main(args)
