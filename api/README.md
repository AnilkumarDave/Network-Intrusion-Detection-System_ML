# API Layer for Network Intrusion Detection System (NIDS)

This folder contains a small Flask-based REST API that exposes the trained
Network Intrusion Detection System (NIDS) model so that other systems and
test tools can query it.

The main goals are to:

- Provide a simple `/health` endpoint to confirm the service is running  
- Provide a `/predict` endpoint which accepts JSON with feature values and
  returns an intrusion/normal prediction  
- Make it easy to test the model using tools such as Postman, curl and
  Java RestAssured tests

## Endpoints

- `GET /health`  
  - Returns HTTP 200 and a small JSON body such as `{"status": "ok"}`  

- `POST /predict`  
  - Expects JSON input containing the features required by the trained model  
  - Returns a JSON response with fields such as `prediction` and
    optionally `probabilities` or `class_name`  

Example request body (Anil can adapt to his feature set):

```json
{
  "features": [0.1, 0.0, 1.2, 3.4, 0.0, 5.6]
}
```

Example response:

```json
{
  "prediction": 1,
  "class_name": "attack",
  "probabilities": [0.1, 0.9]
}
```

## Running the API

From the `api` folder:

```bash
pip install -r requirements.txt
python app.py
```

By default, the API will listen on `http://127.0.0.1:5000`.

## Notes for Anil

- Update the model loading path in `app.py` so it points to the actual saved model
  (for example, `models/best_model.pkl`).  
- Adjust the feature preprocessing and response formatting to match the model
  and notebook code used in the project.
