from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# ------------------------------------------------------------------
# UPDATE THIS FILENAME ONLY if your best model is different
# Example options: "KNN.joblib", "RandomForest.joblib", "XGBoost.joblib"
# ------------------------------------------------------------------
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "results",
    "models",
    "KNN.joblib"   # <-- change this to the model you want to serve
)

model = None

def load_model():
    """Loads the ML model once (lazy loading)."""
    global model
    if model is None:
        resolved = os.path.abspath(MODEL_PATH)
        if not os.path.exists(resolved):
            raise FileNotFoundError(f"Model file not found at: {resolved}")
        model = joblib.load(resolved)
        print(f"[INFO] Model loaded from: {resolved}")


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict endpoint: expects JSON like:
    {
        "features": [0.1, 0.2, ...]
    }
    """
    load_model()

    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "JSON must contain a 'features' field."}), 400

    features = data["features"]

    # Convert to numpy
    try:
        features = np.array(features).reshape(1, -1)
    except Exception:
        return jsonify({"error": "Invalid feature format. Must be a list of numbers."}), 400

    # Predict
    pred = model.predict(features)
    response = {"prediction": int(pred[0])}

    # If model supports probability output
    if hasattr(model, "predict_proba"):
        try:
            probs = model.predict_proba(features)[0].tolist()
            response["probabilities"] = probs
        except Exception:
            pass

    return jsonify(response), 200


if __name__ == "__main__":
    # Local test server (not for production)
    app.run(host="127.0.0.1", port=5000, debug=True)
