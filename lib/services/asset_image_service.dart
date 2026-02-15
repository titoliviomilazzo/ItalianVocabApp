import 'dart:convert';
import 'package:flutter/services.dart';
import '../models/word.dart';

class AssetImageService {
  static Set<String>? _normalizedAssetPaths;

  static Future<Set<String>> _loadAssetPaths() async {
    if (_normalizedAssetPaths != null) return _normalizedAssetPaths!;

    final manifestJson = await rootBundle.loadString('AssetManifest.json');
    final Map<String, dynamic> manifestMap =
        json.decode(manifestJson) as Map<String, dynamic>;

    // Flutter web can expose keys like `assets/assets/...`.
    // Normalize to `assets/...` so app paths match consistently.
    _normalizedAssetPaths = manifestMap.keys.map(_normalizeAssetKey).toSet();
    return _normalizedAssetPaths!;
  }

  static Future<String?> resolveWordImagePath(Word word) async {
    final assetPaths = await _loadAssetPaths();
    final id = word.id;
    final paddedId = id.toString().padLeft(3, '0');
    final slug = _slugify(word.word);

    final candidates = <String>[
      word.imagePath,
      'assets/images/$id.webp',
      'assets/images/$id.png',
      'assets/images/$id.jpg',
      'assets/images/$id.jpeg',
      'assets/images/${id}_$slug.webp',
      'assets/images/${id}_$slug.png',
      'assets/images/${id}_$slug.jpg',
      'assets/images/${id}_$slug.jpeg',
      'assets/images/${paddedId}_$slug.webp',
      'assets/images/${paddedId}_$slug.png',
      'assets/images/${paddedId}_$slug.jpg',
      'assets/images/${paddedId}_$slug.jpeg',
    ];

    for (final path in candidates) {
      if (assetPaths.contains(path)) return path;
    }

    final idPrefix = 'assets/images/${id}_';
    final paddedPrefix = 'assets/images/${paddedId}_';

    final prefixedMatches = assetPaths
        .where((p) => p.startsWith(idPrefix) || p.startsWith(paddedPrefix))
        .toList();

    if (prefixedMatches.isEmpty) return null;

    const extPriority = ['.png', '.jpg', '.jpeg', '.webp'];
    for (final ext in extPriority) {
      for (final match in prefixedMatches) {
        if (match.toLowerCase().endsWith(ext)) return match;
      }
    }

    return prefixedMatches.first;
  }

  static String _slugify(String input) {
    var value = input.toLowerCase();
    value = value.replaceAll(RegExp(r'[^a-z0-9]+'), '_');
    value = value.replaceAll(RegExp(r'_+'), '_');
    value = value.replaceAll(RegExp(r'^_|_$'), '');
    return value;
  }

  static String _normalizeAssetKey(String key) {
    if (key.startsWith('assets/assets/')) {
      return key.replaceFirst('assets/assets/', 'assets/');
    }
    return key;
  }
}
