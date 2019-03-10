package com.example.shipkitworkshop;

import java.math.BigDecimal;

public class MathUtils {

    public static boolean isTriangle(int a, int b, int c) {
        return a + b > c
                && a + c > b
                && b + c > a;
    }

    public static boolean isTriangle(long a, long b, long c) {
        return a + b > c
                && a + c > b
                && b + c > a;
    }

    public static boolean isTriangle(float a, float b, float c) {
        return a + b > c
                && a + c > b
                && b + c > a;
    }

    public static boolean isTriangle(BigDecimal a, BigDecimal b, BigDecimal c) {
        return a.add(b).compareTo(c) > 0
                && a.add(c).compareTo(b) > 0
                && b.add(c).compareTo(a) > 0;
    }
}
