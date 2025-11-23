# API Test Automation for NIDS

This folder contains a small Java project used to test the Flask-based API
exposed by the Network Intrusion Detection System (NIDS).

The goals are to:

- Verify that the `/health` endpoint is reachable and returns HTTP 200  
- Verify that the `/predict` endpoint returns HTTP 200 and JSON for valid input  
- Demonstrate the use of JUnit 5 and RestAssured in the context of a security/ML project

## Project structure

- `pom.xml` – Maven configuration, dependencies (JUnit 5, RestAssured)  
- `src/test/java/com/anildave/nidsapi/tests/NidsApiTest.java` – example tests

## Prerequisites

- JDK 11+ installed  
- Maven installed (`mvn -v` should work)  
- The Flask API running locally, e.g.: `http://127.0.0.1:5000`

## How to run tests

From the `automation` folder:

```bash
mvn clean test
```

By default, the tests assume the API is available at `http://127.0.0.1:5000`.
You can change this by editing the `BASE_URL` constant in `NidsApiTest.java`.
