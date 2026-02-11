// import 'package:shared_preferences/shared_preferences.dart';

class StorageService {
  // static const String _learnedWordsKey = 'learned_words';
  final Set<int> _learnedWords = {};

  Future<void> saveLearnedWord(int id) async {
    _learnedWords.add(id);
    // final prefs = await SharedPreferences.getInstance();
    // final List<String> learned = prefs.getStringList(_learnedWordsKey) ?? [];
    // if (!learned.contains(id.toString())) {
    //   learned.add(id.toString());
    //   await prefs.setStringList(_learnedWordsKey, learned);
    // }
  }

  Future<void> removeLearnedWord(int id) async {
    _learnedWords.remove(id);
    // final prefs = await SharedPreferences.getInstance();
    // final List<String> learned = prefs.getStringList(_learnedWordsKey) ?? [];
    // if (learned.contains(id.toString())) {
    //   learned.remove(id.toString());
    //   await prefs.setStringList(_learnedWordsKey, learned);
    // }
  }

  Future<List<int>> getLearnedWords() async {
    return _learnedWords.toList();
    // final prefs = await SharedPreferences.getInstance();
    // final List<String> learned = prefs.getStringList(_learnedWordsKey) ?? [];
    // return learned.map((e) => int.parse(e)).toList();
  }
}
