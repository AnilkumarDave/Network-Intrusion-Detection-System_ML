package com.anildave.nidsapi.tests;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

public class NidsApiTest {

    private static final String BASE_URL = "http://127.0.0.1:5000";

    @BeforeAll
    static void configureRestAssured() {
        RestAssured.baseURI = BASE_URL;
    }

    @Test
    void healthEndpointReturnsOk() {
        given()
            .when()
                .get("/health")
            .then()
                .statusCode(200)
                .contentType(ContentType.JSON)
                .body("status", equalTo("ok"));
    }

    @Test
    void predictEndpointReturnsOkForValidInput() {
        // Example feature list – Anil should adjust to match the actual model features
        double[] features = new double[] {
                0.0, 1.0, 0.0, 0.5, 0.2, 0.0, 0.0, 0.1, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0,
                0.1, 0.0, 0.0, 0.0, 0.0, 0.6, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.2
        };

        given()
            .contentType(ContentType.JSON)
            .body("{"features": [" + join(features) + "]}")
        .when()
            .post("/predict")
        .then()
            .statusCode(200)
            .contentType(ContentType.JSON)
            .body("prediction", notNullValue());
    }

    private static String join(double[] values) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            sb.append(values[i]);
            if (i < values.length - 1) {
                sb.append(",");
            }
        }
        return sb.toString();
    }
}
