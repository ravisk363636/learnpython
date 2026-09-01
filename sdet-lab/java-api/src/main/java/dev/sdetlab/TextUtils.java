package dev.sdetlab;

import java.util.Locale;
import java.util.Objects;

/** Small production-shaped helper so week 1 includes unit tests, not only API calls. */
public final class TextUtils {

  private TextUtils() {}

  public static String normalizeTitle(String value) {
    Objects.requireNonNull(value, "value");
    return value.trim().toLowerCase(Locale.ROOT);
  }
}
