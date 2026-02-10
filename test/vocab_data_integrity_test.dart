import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:italian_vocab_app/models/word.dart';

void main() {
  test('vocab.json file should exist and contain valid data', () async {
    final file = File('assets/data/vocab.json');
    expect(await file.exists(), isTrue, reason: 'vocab.json file not found');

    final jsonString = await file.readAsString();
    final List<dynamic> jsonList = json.decode(jsonString);

    expect(jsonList.isNotEmpty, isTrue, reason: 'vocab.json is empty');
    print('Total words found: ${jsonList.length}');

    // Verify first item
    final firstItem = Word.fromJson(jsonList.first);
    expect(firstItem.id, 1);
    expect(firstItem.word, 'a');
    
    // Verify list parsing
    final words = jsonList.map((json) => Word.fromJson(json)).toList();
    expect(words.length, jsonList.length);
    
    // Check for 7244 items as expected from conversion
    expect(words.length, 7244);
  });
}
