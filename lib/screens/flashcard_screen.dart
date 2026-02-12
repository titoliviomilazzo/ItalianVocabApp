import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/word.dart';
import '../widgets/flashcard_widget.dart';
import '../theme/app_theme.dart';

class FlashcardScreen extends StatefulWidget {
  final List<Word> words;
  final int initialIndex;
  final Function(int) onToggleLearned;
  final bool shuffle;

  const FlashcardScreen({
    super.key, 
    required this.words, 
    required this.initialIndex,
    required this.onToggleLearned,
    this.shuffle = false,
  });

  @override
  State<FlashcardScreen> createState() => _FlashcardScreenState();
}

class _FlashcardScreenState extends State<FlashcardScreen> {
  late PageController _pageController;
  late List<Word> _words;
  int _currentIndex = 0;

  @override
  void initState() {
    super.initState();
    _words = List.from(widget.words);
    if (widget.shuffle) {
      _words.shuffle();
      _currentIndex = 0;
      _pageController = PageController(initialPage: 0);
    } else {
      _currentIndex = widget.initialIndex;
      _pageController = PageController(initialPage: widget.initialIndex);
    }
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  void _handleToggleLearned() {
    final currentWord = _words[_currentIndex];
    final newStatus = !currentWord.isLearned;

    setState(() {
      _words[_currentIndex] = currentWord.copyWith(isLearned: newStatus);
    });
    
    widget.onToggleLearned(currentWord.id);
  }

  void _goToPrevious() {
    if (_currentIndex > 0) {
      _pageController.previousPage(
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
      );
    }
  }

  void _goToNext() {
    if (_currentIndex < _words.length - 1) {
      _pageController.nextPage(
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeInOut,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final currentWord = _words[_currentIndex];
    
    return Scaffold(
      backgroundColor: AppTheme.warmCream,
      appBar: AppBar(
        title: Text(
          '${_currentIndex + 1} / ${_words.length}',
          style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 16),
        ),
        flexibleSpace: Container(
          decoration: const BoxDecoration(gradient: AppTheme.appBarGradient),
        ),
        foregroundColor: Colors.white,
        elevation: 0,
        actions: [
          if (widget.shuffle)
            const Padding(
              padding: EdgeInsets.only(right: 4),
              child: Icon(Icons.shuffle, size: 18, color: Colors.white70),
            ),
          IconButton(
            icon: Icon(
              currentWord.isLearned ? Icons.check_circle : Icons.check_circle_outline,
              color: currentWord.isLearned ? const Color(0xFF90EE90) : Colors.white70,
            ),
            tooltip: 'Mark as Learned',
            onPressed: _handleToggleLearned,
          ),
        ],
      ),
      body: PageView.builder(
        controller: _pageController,
        itemCount: _words.length,
        onPageChanged: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        itemBuilder: (context, index) {
          return Center(
            child: FlashcardWidget(word: _words[index]),
          );
        },
      ),
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          color: AppTheme.warmCream,
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.04),
              blurRadius: 8,
              offset: const Offset(0, -2),
            ),
          ],
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 10),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                IconButton(
                  onPressed: _currentIndex > 0 ? _goToPrevious : null,
                  icon: const Icon(Icons.arrow_back_ios_rounded),
                  iconSize: 26,
                  color: AppTheme.terracotta,
                  disabledColor: AppTheme.warmGrey.withValues(alpha: 0.3),
                  tooltip: '이전 카드',
                ),
                Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      _words[_currentIndex].word,
                      style: GoogleFonts.outfit(
                        fontSize: 16,
                        color: AppTheme.darkEspresso,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                    if (_words[_currentIndex].meaning.isNotEmpty)
                      Text(
                        _words[_currentIndex].meaning,
                        style: GoogleFonts.inter(
                          fontSize: 12,
                          color: AppTheme.warmGrey,
                        ),
                      ),
                  ],
                ),
                IconButton(
                  onPressed: _currentIndex < _words.length - 1 ? _goToNext : null,
                  icon: const Icon(Icons.arrow_forward_ios_rounded),
                  iconSize: 26,
                  color: AppTheme.terracotta,
                  disabledColor: AppTheme.warmGrey.withValues(alpha: 0.3),
                  tooltip: '다음 카드',
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
