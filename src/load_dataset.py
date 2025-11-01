import pandas as pd
from pathlib import Path

# Define file paths
data_dir = Path("data")
train_path = data_dir / "KDDTrain+.txt"
test_path  = data_dir / "KDDTest+.txt"

def smart_read(path):
    """Try to load the dataset using comma or tab as separator."""
    for sep in [",", "\t"]:
        try:
            df = pd.read_csv(path, sep=sep, header=None, low_memory=False)
            if df.shape[1] >= 41:  # expected columns for NSL-KDD
                print(f"✅ Loaded {path.name} with sep='{sep}', shape={df.shape}")
                return df
        except Exception:
            continue
    df = pd.read_csv(path, header=None, engine="python", sep=None)
    print(f"✅ Loaded {path.name} (auto sep), shape={df.shape}")
    return df

# Load datasets
train_df = smart_read(train_path)
test_df  = smart_read(test_path)

# Preview sample data
print("\n🔹 Train dataset preview:")
print(train_df.head().to_string(index=False))

# (Optional) Save them as CSV for easier re-use
train_df.to_csv("data/KDDTrain_converted.csv", index=False)
test_df.to_csv("data/KDDTest_converted.csv", index=False)

print("\n💾 Saved cleaned copies as:")
print(" - data/KDDTrain_converted.csv")
print(" - data/KDDTest_converted.csv")
