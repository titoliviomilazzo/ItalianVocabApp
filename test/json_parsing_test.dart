import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:italian_vocab_app/models/word.dart';

void main() {
  test('Word.fromJson parses valid JSON correctly', () {
    const jsonString = '''
      {
        "id": 1,
        "word": "Consapevolezza",
        "gender": "f.",
        "level": "B2.1",
        "meaning": "인식, 의식",
        "pronunciation": "콘사페볼레짜",
        "image_path": "assets/images/1.webp"
      }
    ''';

    final Map<String, dynamic> jsonMap = json.decode(jsonString);
    final word = Word.fromJson(jsonMap);

    expect(word.id, 1);
    expect(word.word, "Consapevolezza");
    expect(word.gender, "f.");
    expect(word.level, "B2.1");
    expect(word.meaning, "인식, 의식");
    expect(word.pronunciation, "콘사페볼레짜");
    expect(word.imagePath, "assets/images/1.webp");
  });
}
