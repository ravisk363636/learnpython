package dev.sdetlab;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.greaterThan;
import static org.hamcrest.Matchers.notNullValue;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class JsonPlaceholderApiTest {

  @BeforeAll
  static void setup() {
    RestAssured.baseURI = "https://jsonplaceholder.typicode.com";
  }

  @Test
  void getPostReturnsExpectedResource() {
    given()
        .when()
        .get("/posts/1")
        .then()
        .statusCode(200)
        .contentType(ContentType.JSON)
        .body("id", equalTo(1))
        .body("userId", equalTo(1))
        .body("title", notNullValue());
  }

  @Test
  void listPostsReturnsACollection() {
    given()
        .when()
        .get("/posts")
        .then()
        .statusCode(200)
        .body("size()", greaterThan(1));
  }

  @Test
  void createPostReturnsCreatedPayload() {
    given()
        .contentType(ContentType.JSON)
        .body("{\"title\":\"sdet-lab\",\"body\":\"week-1\",\"userId\":1}")
        .when()
        .post("/posts")
        .then()
        .statusCode(201)
        .body("title", equalTo("sdet-lab"))
        .body("id", notNullValue());
  }
}
