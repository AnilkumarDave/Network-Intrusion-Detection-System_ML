import pandas as pd
import numpy as np
import argparse
import os
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib

# ---------------------------
# Helper Functions
# ---------------------------

def load_data(train_path, test_path):
    """Load NSL-KDD train and test datasets."""
    print(f"Loading train: {train_path}")
    df_train = pd.read_csv(train_path, header=None)
    print(f"Loading test: {test_path}")
    df_test = pd.read_csv(test_path, header=None)
    return df_train, df_test


def assign_column_names(df):
    """Assign column names based on NSL-KDD dataset definition (includes 'difficulty')."""
    columns = [
        'duration','protocol_type','service','flag','src_bytes','dst_bytes',
        'land','wrong_fragment','urgent','hot','num_failed_logins','logged_in',
        'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
        'num_shells','num_access_files','num_outbound_cmds','is_host_login',
        'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
        'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
        'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
        'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
        'dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty'
    ]
    df.columns = columns
    return df



def map_binary_label(df):
    """Convert multi-class labels into binary: 0 (normal) and 1 (attack)."""
    df['label'] = df['label'].astype(str).str.strip().str.lower()
    df['binary_label'] = df['label'].apply(lambda x: 0 if 'normal' in x else 1)

    print("\nLabel value counts:")
    print(df['binary_label'].value_counts())
    return df


def encode_and_scale(train_df, test_df):
    """Encode categorical features and scale numeric ones."""
    categorical_cols = ['protocol_type', 'service', 'flag']

    # One-hot encode categorical columns
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    encoder.fit(train_df[categorical_cols])

    train_encoded = pd.DataFrame(encoder.transform(train_df[categorical_cols]),
                                 columns=encoder.get_feature_names_out(categorical_cols))
    test_encoded = pd.DataFrame(encoder.transform(test_df[categorical_cols]),
                                columns=encoder.get_feature_names_out(categorical_cols))

    # Drop original categorical columns and add encoded ones
    train_df = pd.concat([train_df.drop(columns=categorical_cols), train_encoded], axis=1)
    test_df = pd.concat([test_df.drop(columns=categorical_cols), test_encoded], axis=1)

    # Identify numeric feature columns (exclude labels)
    feature_cols = [col for col in train_df.columns if col not in ['label', 'binary_label']]

    # Scale features
    scaler = StandardScaler()
    scaler.fit(pd.concat([train_df[feature_cols], test_df[feature_cols]], axis=0))

    train_df[feature_cols] = scaler.transform(train_df[feature_cols])
    test_df[feature_cols] = scaler.transform(test_df[feature_cols])

    print("\n✅ All features are numeric!\n")
    return train_df, test_df, encoder, scaler


def main(args):
    df_train, df_test = load_data(args.train, args.test)

    df_train = assign_column_names(df_train)
    df_test = assign_column_names(df_test)

    df_train = map_binary_label(df_train)
    df_test = map_binary_label(df_test)

    df_train, df_test, encoder, scaler = encode_and_scale(df_train, df_test)

    os.makedirs("results", exist_ok=True)

    df_train.to_csv("results/processed_train.csv", index=False)
    df_test.to_csv("results/processed_test.csv", index=False)
    joblib.dump(encoder, "results/encoder.pkl")
    joblib.dump(scaler, "results/scaler.pkl")

    print("✅ Preprocessing complete!")
    print("Processed training saved to results/processed_train.csv")
    print("Processed test saved to results/processed_test.csv")
    print("Encoders and scaler saved to results/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", default="data/KDDTrain+.txt")
    parser.add_argument("--test", default="data/KDDTest+.txt")
    args = parser.parse_args()
    main(args)
