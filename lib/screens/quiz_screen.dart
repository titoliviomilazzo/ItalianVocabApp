import 'dart:math';
import 'package:flutter/material.dart';
import '../models/word.dart';
import '../services/tts_service.dart';

class QuizScreen extends StatefulWidget {
  final List<Word> words;

  const QuizScreen({super.key, required this.words});

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  late List<Word> _quizWords;
  late List<Word> _allWordsWithMeaning;
  int _currentIndex = 0;
  int _score = 0;
  int _totalAnswered = 0;
  int? _selectedOptionIndex;
  bool _answered = false;
  late List<String> _options;
  late int _correctOptionIndex;
  final Random _random = Random();

  @override
  void initState() {
    super.initState();
    // Only use words that have meanings
    _allWordsWithMeaning = widget.words
        .where((w) => w.meaning.isNotEmpty)
        .toList();
    _quizWords = List.from(_allWordsWithMeaning)..shuffle(_random);
    
    // Limit to 20 questions per session
    if (_quizWords.length > 20) {
      _quizWords = _quizWords.sublist(0, 20);
    }
    
    _generateOptions();
  }

  void _generateOptions() {
    final correctWord = _quizWords[_currentIndex];
    final correctMeaning = correctWord.meaning;

    // Get 3 wrong answers from all words with meaning
    final wrongWords = _allWordsWithMeaning
        .where((w) => w.id != correctWord.id && w.meaning.isNotEmpty)
        .toList()
      ..shuffle(_random);
    
    final wrongMeanings = wrongWords
        .take(3)
        .map((w) => w.meaning)
        .toList();

    _options = [correctMeaning, ...wrongMeanings]..shuffle(_random);
    _correctOptionIndex = _options.indexOf(correctMeaning);
    _selectedOptionIndex = null;
    _answered = false;
  }

  void _handleOptionTap(int index) {
    if (_answered) return;

    setState(() {
      _selectedOptionIndex = index;
      _answered = true;
      _totalAnswered++;
      if (index == _correctOptionIndex) {
        _score++;
      }
    });
  }

  void _nextQuestion() {
    if (_currentIndex < _quizWords.length - 1) {
      setState(() {
        _currentIndex++;
        _generateOptions();
      });
    } else {
      _showResults();
    }
  }

  void _showResults() {
    final percentage = (_score / _totalAnswered * 100).round();
    String emoji;
    String message;
    
    if (percentage >= 90) {
      emoji = '🏆';
      message = '완벽해요!';
    } else if (percentage >= 70) {
      emoji = '👏';
      message = '잘했어요!';
    } else if (percentage >= 50) {
      emoji = '💪';
      message = '조금 더 노력해봐요!';
    } else {
      emoji = '📚';
      message = '복습이 필요해요!';
    }

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: Text('$emoji 퀴즈 결과', style: const TextStyle(fontSize: 24)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              '$_score / $_totalAnswered',
              style: const TextStyle(fontSize: 48, fontWeight: FontWeight.bold, color: Colors.indigo),
            ),
            const SizedBox(height: 8),
            Text(
              '$percentage% 정답률',
              style: TextStyle(fontSize: 18, color: Colors.grey[600]),
            ),
            const SizedBox(height: 16),
            Text(
              message,
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w500),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.of(context).pop();
              Navigator.of(context).pop();
            },
            child: const Text('홈으로'),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.of(context).pop();
              setState(() {
                _currentIndex = 0;
                _score = 0;
                _totalAnswered = 0;
                _quizWords = List.from(_allWordsWithMeaning)..shuffle(_random);
                if (_quizWords.length > 20) {
                  _quizWords = _quizWords.sublist(0, 20);
                }
                _generateOptions();
              });
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.indigo,
              foregroundColor: Colors.white,
            ),
            child: const Text('다시 도전'),
          ),
        ],
      ),
    );
  }

  Color _getOptionColor(int index) {
    if (!_answered) return Colors.white;
    if (index == _correctOptionIndex) return Colors.green.shade50;
    if (index == _selectedOptionIndex) return Colors.red.shade50;
    return Colors.white;
  }

  Color _getOptionBorderColor(int index) {
    if (!_answered) {
      return index == _selectedOptionIndex ? Colors.indigo : Colors.grey.shade300;
    }
    if (index == _correctOptionIndex) return Colors.green;
    if (index == _selectedOptionIndex) return Colors.red;
    return Colors.grey.shade300;
  }

  IconData? _getOptionIcon(int index) {
    if (!_answered) return null;
    if (index == _correctOptionIndex) return Icons.check_circle;
    if (index == _selectedOptionIndex && index != _correctOptionIndex) return Icons.cancel;
    return null;
  }

  @override
  Widget build(BuildContext context) {
    if (_quizWords.isEmpty) {
      return Scaffold(
        appBar: AppBar(
          title: const Text('퀴즈'),
          backgroundColor: Colors.indigo,
          foregroundColor: Colors.white,
        ),
        body: const Center(
          child: Text('의미가 있는 단어가 부족합니다.\n먼저 단어 데이터를 보강해 주세요.',
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 18)),
        ),
      );
    }

    final currentWord = _quizWords[_currentIndex];

    return Scaffold(
      appBar: AppBar(
        title: Text('퀴즈 ${_currentIndex + 1}/${_quizWords.length}'),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
        actions: [
          Center(
            child: Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Text(
                '✅ $_score / $_totalAnswered',
                style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
            ),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            // Progress bar
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: LinearProgressIndicator(
                value: (_currentIndex + 1) / _quizWords.length,
                minHeight: 8,
                backgroundColor: Colors.grey[200],
                valueColor: const AlwaysStoppedAnimation<Color>(Colors.indigo),
              ),
            ),
            const SizedBox(height: 20),

            // Word display
            Card(
              elevation: 4,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 20),
                child: Column(
                  children: [
                    Text(
                      currentWord.word,
                      style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      currentWord.gender,
                      style: TextStyle(fontSize: 13, color: Colors.grey[500]),
                    ),
                    const SizedBox(height: 8),
                    GestureDetector(
                      onTap: () => TtsService.speak(currentWord.word),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                        decoration: BoxDecoration(
                          color: Colors.indigo.withValues(alpha: 0.1),
                          borderRadius: BorderRadius.circular(20),
                        ),
                        child: const Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(Icons.volume_up, color: Colors.indigo, size: 18),
                            SizedBox(width: 4),
                            Text('발음 듣기', style: TextStyle(color: Colors.indigo, fontWeight: FontWeight.w500, fontSize: 13)),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),

            // Question label
            const Text(
              '이 단어의 뜻은?',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.w500, color: Colors.black54),
            ),
            const SizedBox(height: 12),

            // Options
            ...List.generate(4, (index) {
              final icon = _getOptionIcon(index);
              return Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: InkWell(
                  onTap: () => _handleOptionTap(index),
                  borderRadius: BorderRadius.circular(12),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 300),
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                    decoration: BoxDecoration(
                      color: _getOptionColor(index),
                      border: Border.all(
                        color: _getOptionBorderColor(index),
                        width: 2,
                      ),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 28,
                          height: 28,
                          decoration: BoxDecoration(
                            color: Colors.indigo.withValues(alpha: 0.1),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Center(
                            child: Text(
                              String.fromCharCode(65 + index), // A, B, C, D
                              style: const TextStyle(
                                fontWeight: FontWeight.bold,
                                color: Colors.indigo,
                                fontSize: 13,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            _options[index],
                            style: const TextStyle(fontSize: 15),
                          ),
                        ),
                        if (icon != null)
                          Icon(
                            icon,
                            color: index == _correctOptionIndex ? Colors.green : Colors.red,
                          ),
                      ],
                    ),
                  ),
                ),
              );
            }),
          ],
        ),
      ),
      // Next button always visible at the bottom
      bottomNavigationBar: _answered
          ? SafeArea(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(20, 8, 20, 16),
                child: SizedBox(
                  width: double.infinity,
                  height: 50,
                  child: ElevatedButton(
                    onPressed: _nextQuestion,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.indigo,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    ),
                    child: Text(
                      _currentIndex < _quizWords.length - 1 ? '다음 문제' : '결과 보기',
                      style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
              ),
            )
          : null,
    );
  }
}
