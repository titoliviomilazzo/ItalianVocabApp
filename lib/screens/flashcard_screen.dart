import 'package:flutter/material.dart';
import '../models/word.dart';
import '../widgets/flashcard_widget.dart';

class FlashcardScreen extends StatefulWidget {
  final List<Word> words;
  final int initialIndex;

  const FlashcardScreen({super.key, required this.words, required this.initialIndex});

  @override
  State<FlashcardScreen> createState() => _FlashcardScreenState();
}

class _FlashcardScreenState extends State<FlashcardScreen> {
  late PageController _pageController;

  @override
  void initState() {
    super.initState();
    _pageController = PageController(initialPage: widget.initialIndex);
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flashcards'),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
      ),
      body: PageView.builder(
        controller: _pageController,
        itemCount: widget.words.length,
        itemBuilder: (context, index) {
          return Center(
            child: FlashcardWidget(word: widget.words[index]),
          );
        },
      ),
    );
  }
}
