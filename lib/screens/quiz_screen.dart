import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/word.dart';
import '../services/tts_service.dart';
import '../theme/app_theme.dart';

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
    _allWordsWithMeaning = widget.words
        .where((w) => w.meaning.isNotEmpty)
        .toList();
    _quizWords = List.from(_allWordsWithMeaning)..shuffle(_random);
    
    if (_quizWords.length > 20) {
      _quizWords = _quizWords.sublist(0, 20);
    }
    
    _generateOptions();
  }

  void _generateOptions() {
    final correctWord = _quizWords[_currentIndex];
    final correctMeaning = correctWord.meaning;

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
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        backgroundColor: AppTheme.warmCream,
        title: Text('$emoji 퀴즈 결과', style: GoogleFonts.outfit(fontSize: 24)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              '$_score / $_totalAnswered',
              style: GoogleFonts.outfit(
                fontSize: 48,
                fontWeight: FontWeight.bold,
                color: AppTheme.terracotta,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              '$percentage% 정답률',
              style: GoogleFonts.inter(fontSize: 18, color: AppTheme.warmGrey),
            ),
            const SizedBox(height: 16),
            Text(
              message,
              style: GoogleFonts.inter(fontSize: 20, fontWeight: FontWeight.w500),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.of(context).pop();
              Navigator.of(context).pop();
            },
            child: Text('홈으로', style: TextStyle(color: AppTheme.warmGrey)),
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
              backgroundColor: AppTheme.terracotta,
              foregroundColor: Colors.white,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            ),
            child: const Text('다시 도전'),
          ),
        ],
      ),
    );
  }

  Color _getOptionColor(int index) {
    if (!_answered) return AppTheme.softWhite;
    if (index == _correctOptionIndex) return AppTheme.oliveGreen.withValues(alpha: 0.1);
    if (index == _selectedOptionIndex) return AppTheme.terracotta.withValues(alpha: 0.1);
    return AppTheme.softWhite;
  }

  Color _getOptionBorderColor(int index) {
    if (!_answered) {
      return index == _selectedOptionIndex ? AppTheme.terracotta : Colors.grey.shade200;
    }
    if (index == _correctOptionIndex) return AppTheme.oliveGreen;
    if (index == _selectedOptionIndex) return AppTheme.terracotta;
    return Colors.grey.shade200;
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
        backgroundColor: AppTheme.warmCream,
        appBar: AppBar(
          title: Text('퀴즈', style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
          flexibleSpace: Container(decoration: const BoxDecoration(gradient: AppTheme.appBarGradient)),
          foregroundColor: Colors.white,
        ),
        body: Center(
          child: Text('의미가 있는 단어가 부족합니다.\n먼저 단어 데이터를 보강해 주세요.',
            textAlign: TextAlign.center,
            style: GoogleFonts.inter(fontSize: 18, color: AppTheme.warmGrey)),
        ),
      );
    }

    final currentWord = _quizWords[_currentIndex];

    return Scaffold(
      backgroundColor: AppTheme.warmCream,
      appBar: AppBar(
        title: Text(
          '퀴즈 ${_currentIndex + 1}/${_quizWords.length}',
          style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 16),
        ),
        flexibleSpace: Container(decoration: const BoxDecoration(gradient: AppTheme.appBarGradient)),
        foregroundColor: Colors.white,
        elevation: 0,
        actions: [
          Center(
            child: Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Text(
                  '✅ $_score / $_totalAnswered',
                  style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.bold, color: Colors.white),
                ),
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
                minHeight: 6,
                backgroundColor: AppTheme.lightTerracotta,
                valueColor: const AlwaysStoppedAnimation<Color>(AppTheme.terracotta),
              ),
            ),
            const SizedBox(height: 24),

            // Word display
            Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 20),
              decoration: AppTheme.cardDecoration,
              child: Column(
                children: [
                  Text(
                    currentWord.word,
                    style: GoogleFonts.outfit(
                      fontSize: 32,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.darkEspresso,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    currentWord.gender,
                    style: GoogleFonts.inter(
                      fontSize: 13,
                      color: AppTheme.warmGrey,
                      fontStyle: FontStyle.italic,
                    ),
                  ),
                  const SizedBox(height: 12),
                  GestureDetector(
                    onTap: () => TtsService.speak(currentWord.word),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                      decoration: BoxDecoration(
                        color: AppTheme.terracotta.withValues(alpha: 0.1),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.volume_up_rounded, color: AppTheme.terracotta, size: 18),
                          const SizedBox(width: 4),
                          Text('발음 듣기', style: GoogleFonts.inter(color: AppTheme.terracotta, fontWeight: FontWeight.w500, fontSize: 13)),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            // Question label
            Text(
              '이 단어의 뜻은?',
              style: GoogleFonts.inter(fontSize: 15, fontWeight: FontWeight.w500, color: AppTheme.warmGrey),
            ),
            const SizedBox(height: 14),

            // Options
            ...List.generate(4, (index) {
              final icon = _getOptionIcon(index);
              return Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: InkWell(
                  onTap: () => _handleOptionTap(index),
                  borderRadius: BorderRadius.circular(14),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 300),
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                    decoration: BoxDecoration(
                      color: _getOptionColor(index),
                      border: Border.all(
                        color: _getOptionBorderColor(index),
                        width: 1.5,
                      ),
                      borderRadius: BorderRadius.circular(14),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withValues(alpha: 0.03),
                          blurRadius: 6,
                          offset: const Offset(0, 2),
                        ),
                      ],
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 30,
                          height: 30,
                          decoration: BoxDecoration(
                            color: AppTheme.terracotta.withValues(alpha: 0.08),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Center(
                            child: Text(
                              String.fromCharCode(65 + index),
                              style: GoogleFonts.inter(
                                fontWeight: FontWeight.bold,
                                color: AppTheme.terracotta,
                                fontSize: 13,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            _options[index],
                            style: GoogleFonts.inter(fontSize: 15, color: AppTheme.darkEspresso),
                          ),
                        ),
                        if (icon != null)
                          Icon(
                            icon,
                            color: index == _correctOptionIndex ? AppTheme.oliveGreen : AppTheme.terracotta,
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
      bottomNavigationBar: _answered
          ? Container(
              decoration: BoxDecoration(
                color: AppTheme.warmCream,
                boxShadow: [
                  BoxShadow(color: Colors.black.withValues(alpha: 0.04), blurRadius: 8, offset: const Offset(0, -2)),
                ],
              ),
              child: SafeArea(
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(20, 8, 20, 10),
                  child: SizedBox(
                    width: double.infinity,
                    height: 50,
                    child: ElevatedButton(
                      onPressed: _nextQuestion,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppTheme.terracotta,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                      ),
                      child: Text(
                        _currentIndex < _quizWords.length - 1 ? '다음 문제' : '결과 보기',
                        style: GoogleFonts.inter(fontSize: 17, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                ),
              ),
            )
          : null,
    );
  }
}
