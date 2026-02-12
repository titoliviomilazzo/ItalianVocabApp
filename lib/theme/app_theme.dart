import 'package:flutter/material.dart';

/// Italian-themed color palette and design system for Dammi Parole
class AppTheme {
  // ── Colors ──────────────────────────────────────────────
  static const Color terracotta = Color(0xFFC75B39);
  static const Color oliveGreen = Color(0xFF6B8E23);
  static const Color goldenAmber = Color(0xFFD4A017);
  static const Color warmCream = Color(0xFFFFF8F0);
  static const Color softWhite = Color(0xFFFFFFFF);
  static const Color darkEspresso = Color(0xFF2C1810);
  static const Color deepWine = Color(0xFF8B2252);
  static const Color warmGrey = Color(0xFF8B7D6B);
  static const Color lightTerracotta = Color(0xFFF5E6E0);

  // Level colors
  static const Color fondamentale = Color(0xFF4CAF50);
  static const Color altoUso = Color(0xFFFF9800);
  static const Color altaDisponibilita = Color(0xFF42A5F5);

  // ── Gradients ───────────────────────────────────────────
  static const LinearGradient appBarGradient = LinearGradient(
    colors: [deepWine, terracotta],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient cardGradient = LinearGradient(
    colors: [Color(0xFFFFFBF5), Color(0xFFF8F0E8)],
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
  );

  static const LinearGradient accentGradient = LinearGradient(
    colors: [terracotta, goldenAmber],
    begin: Alignment.centerLeft,
    end: Alignment.centerRight,
  );

  // ── Card Decorations ────────────────────────────────────
  static BoxDecoration get cardDecoration => BoxDecoration(
        gradient: cardGradient,
        borderRadius: BorderRadius.circular(24),
        boxShadow: [
          BoxShadow(
            color: terracotta.withValues(alpha: 0.15),
            blurRadius: 20,
            offset: const Offset(0, 8),
          ),
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.05),
            blurRadius: 10,
            offset: const Offset(0, 2),
          ),
        ],
      );

  static BoxDecoration get listTileDecoration => BoxDecoration(
        color: softWhite,
        borderRadius: BorderRadius.circular(14),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.04),
            blurRadius: 8,
            offset: const Offset(0, 2),
          ),
        ],
      );

  // ── Theme Data ──────────────────────────────────────────
  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      scaffoldBackgroundColor: warmCream,
      colorScheme: ColorScheme.fromSeed(
        seedColor: terracotta,
        primary: terracotta,
        secondary: oliveGreen,
        tertiary: goldenAmber,
        surface: softWhite,
        onPrimary: Colors.white,
        onSecondary: Colors.white,
        onSurface: darkEspresso,
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: terracotta,
        foregroundColor: Colors.white,
        elevation: 0,
        centerTitle: true,
      ),
      cardTheme: CardThemeData(
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          elevation: 0,
          padding: const EdgeInsets.symmetric(vertical: 16),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(14),
          ),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: softWhite,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: BorderSide.none,
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(color: terracotta, width: 1.5),
        ),
        contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 16),
      ),
    );
  }

  // ── Level Colors ────────────────────────────────────────
  static Color getLevelColor(String level) {
    switch (level) {
      case 'Fondamentale':
        return fondamentale;
      case 'Alto Uso':
        return altoUso;
      case 'Alta Disponibilità':
        return altaDisponibilita;
      default:
        return warmGrey;
    }
  }
}
