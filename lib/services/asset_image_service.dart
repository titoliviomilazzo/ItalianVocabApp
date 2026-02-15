import 'dart:convert';
import 'package:flutter/services.dart';
import '../models/word.dart';

class AssetImageService {
  static Set<String>? _assetPaths;

  static Future<Set<String>> _loadAssetPaths() async {
    if (_assetPaths != null) return _assetPaths!;

    final manifestJson = await rootBundle.loadString('AssetManifest.json');
    final Map<String, dynamic> manifestMap =
        json.decode(manifestJson) as Map<String, dynamic>;
    _assetPaths = manifestMap.keys.toSet();
    return _assetPaths!;
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

    const replacements = <String, String>{
      'à': 'a',
      'á': 'a',
      'â': 'a',
      'ä': 'a',
      'ã': 'a',
      'å': 'a',
      'è': 'e',
      'é': 'e',
      'ê': 'e',
      'ë': 'e',
      'ì': 'i',
      'í': 'i',
      'î': 'i',
      'ï': 'i',
      'ò': 'o',
      'ó': 'o',
      'ô': 'o',
      'ö': 'o',
      'õ': 'o',
      'ù': 'u',
      'ú': 'u',
      'û': 'u',
      'ü': 'u',
      'ç': 'c',
      'ñ': 'n',
    };

    replacements.forEach((k, v) {
      value = value.replaceAll(k, v);
    });

    value = value.replaceAll(RegExp(r'[^a-z0-9]+'), '_');
    value = value.replaceAll(RegExp(r'_+'), '_');
    value = value.replaceAll(RegExp(r'^_|_$'), '');
    return value;
  }
}
