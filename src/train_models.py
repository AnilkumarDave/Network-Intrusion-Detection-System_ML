#!/usr/bin/env python3
"""
train_models.py
Train multiple classifiers and save metrics + models.
"""
import os
import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import joblib

# optional imports - may fail if not installed
try:
    import xgboost as xgb
except Exception:
    xgb = None

try:
    import lightgbm as lgb
except Exception:
    lgb = None

from imblearn.over_sampling import SMOTE

def get_models(random_state=42):
    models = {
        "GaussianNB": GaussianNB(),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=random_state, n_jobs=-1),
        "KNN": KNeighborsClassifier(n_neighbors=5, n_jobs=-1),
        "SVC": SVC(probability=True, kernel='rbf', random_state=random_state),
        "AdaBoost": AdaBoostClassifier(n_estimators=50, random_state=random_state)
    }
    if xgb is not None:
        models["XGBoost"] = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', n_jobs=-1, random_state=random_state)
    if lgb is not None:
        models["LightGBM"] = lgb.LGBMClassifier(n_estimators=100, random_state=random_state, n_jobs=-1)
    return models

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    proba = None
    try:
        proba = model.predict_proba(X_test)[:,1]
    except Exception:
        proba = None
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc = roc_auc_score(y_test, proba) if proba is not None else np.nan
    cm = confusion_matrix(y_test, y_pred)
    return {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1, "roc_auc": roc, "confusion_matrix": cm.tolist()}

def main(args):
    os.makedirs("results/models", exist_ok=True)

    # Load processed CSVs
    df_train = pd.read_csv(args.train_csv)
    df_test = pd.read_csv(args.test_csv)

    target = 'binary_label'

    # -----------------------------
    # Select numeric feature columns only
    # -----------------------------
    feature_cols = df_train.select_dtypes(include=[np.number]).columns.tolist()
    feature_cols.remove(target)
    if 'orig_label' in feature_cols:
        feature_cols.remove('orig_label')

    X_train = df_train[feature_cols].values
    X_test = df_test[feature_cols].values

    # Ensure y is integer type
    y_train = df_train[target].astype(int).values
    y_test = df_test[target].astype(int).values

    # -----------------------------
    # Sanity check before SMOTE
    # -----------------------------
    print("Unique classes in y_train:", np.unique(y_train))
    print("Counts in y_train:", np.bincount(y_train))

    if len(np.unique(y_train)) < 2:
        raise ValueError("Training data must have at least 2 classes for SMOTE!")

    # Apply SMOTE to training data
    print("Applying SMOTE to training data...")
    sm = SMOTE(random_state=42)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train)
    print("Before SMOTE:", np.bincount(y_train))
    print("After SMOTE:", np.bincount(y_train_res))

    # Train models
    models = get_models()
    metrics = []

    for name, model in models.items():
        print(f"Training {name} ...")
        model.fit(X_train_res, y_train_res)
        res = evaluate_model(model, X_test, y_test)
        res_row = {
            "model": name,
            "accuracy": res["accuracy"],
            "precision": res["precision"],
            "recall": res["recall"],
            "f1": res["f1"],
            "roc_auc": res["roc_auc"],
            "confusion_matrix": res["confusion_matrix"]
        }
        metrics.append(res_row)

        # Save trained model
        joblib.dump(model, f"results/models/{name}.joblib")
        print(f"{name} saved to results/models/{name}.joblib")

    # Save metrics
    metrics_df = pd.DataFrame(metrics)
    metrics_df.to_csv("results/metrics.csv", index=False)
    print("Saved results/metrics.csv")
    print(metrics_df[["model","accuracy","precision","recall","f1","roc_auc"]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_csv", type=str, default="results/processed_train.csv")
    parser.add_argument("--test_csv", type=str, default="results/processed_test.csv")
    args = parser.parse_args()
    main(args)
