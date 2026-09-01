package dev.sdetlab;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class TextUtilsTest {

  @ParameterizedTest
  @CsvSource({
      "'  Hello World  ', hello world",
      "API, api"
  })
  void normalizeTitleTrimsAndLowercases(String input, String expected) {
    assertThat(TextUtils.normalizeTitle(input)).isEqualTo(expected);
  }

  @Test
  void normalizeTitleRejectsNull() {
    assertThatThrownBy(() -> TextUtils.normalizeTitle(null))
        .isInstanceOf(NullPointerException.class)
        .hasMessage("value");
  }
}
