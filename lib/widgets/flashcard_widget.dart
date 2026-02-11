import 'dart:math';
import 'package:flutter/material.dart';
import '../models/word.dart';
import '../services/tts_service.dart';

class FlashcardWidget extends StatefulWidget {
  final Word word;

  const FlashcardWidget({super.key, required this.word});

  @override
  State<FlashcardWidget> createState() => _FlashcardWidgetState();
}

class _FlashcardWidgetState extends State<FlashcardWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;
  bool _isFront = true;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 400),
      vsync: this,
    );
    _animation = Tween<double>(begin: 0, end: 1).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _flipCard() {
    if (_controller.isAnimating) return;
    _isFront = !_isFront;
    if (_isFront) {
      _controller.reverse();
    } else {
      _controller.forward();
    }
  }

  @override
  void didUpdateWidget(covariant FlashcardWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.word.id != widget.word.id) {
      // Reset to front when word changes
      _isFront = true;
      _controller.reset();
    }
  }

  @override
  Widget build(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;
    final screenHeight = MediaQuery.of(context).size.height;
    final cardWidth = screenWidth * 0.85 > 400 ? 400.0 : screenWidth * 0.85;
    final cardHeight = screenHeight * 0.75;

    return GestureDetector(
      onTap: _flipCard,
      child: AnimatedBuilder(
        animation: _animation,
        builder: (context, child) {
          // Split into two halves so content is never mirrored:
          // Front: 0° → 90° (first half), Back: -90° → 0° (second half)
          double angle;
          final bool showFront = _animation.value < 0.5;
          if (_animation.value <= 0.5) {
            angle = _animation.value * pi; // 0 → π/2
          } else {
            angle = (_animation.value - 1) * pi; // -π/2 → 0
          }
          final transform = Matrix4.identity()
            ..setEntry(3, 2, 0.001)
            ..rotateY(angle);

          return Transform(
            alignment: Alignment.center,
            transform: transform,
            child: Card(
              elevation: 8,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
              ),
              child: Container(
                width: cardWidth,
                height: cardHeight,
                padding: const EdgeInsets.all(12),
                child: showFront ? _buildFront() : _buildBack(),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildFront() {
    return Column(
      children: [
        Expanded(
          flex: 5,
          child: Container(
            width: double.infinity,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(12),
              color: Colors.grey[100],
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Image.asset(
                widget.word.imagePath,
                fit: BoxFit.contain,
                errorBuilder: (context, error, stackTrace) {
                  return const Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.image_not_supported, size: 50, color: Colors.grey),
                      SizedBox(height: 10),
                      Text("No Image Yet", style: TextStyle(color: Colors.grey)),
                    ],
                  );
                },
              ),
            ),
          ),
        ),
        const SizedBox(height: 12),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Flexible(
              child: Text(
                widget.word.word,
                style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
                overflow: TextOverflow.ellipsis,
              ),
            ),
            const SizedBox(width: 8),
            GestureDetector(
              onTap: () {
                TtsService.speak(widget.word.word);
              },
              child: Container(
                padding: const EdgeInsets.all(6),
                decoration: BoxDecoration(
                  color: Colors.blue.withValues(alpha: 0.1),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: const Icon(
                  Icons.volume_up,
                  size: 24,
                  color: Colors.blue,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 4),
        Text(
          widget.word.gender,
          style: TextStyle(fontSize: 14, color: Colors.grey[600]),
        ),
        const SizedBox(height: 4),
      ],
    );
  }

  Widget _buildBack() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            '뜻 (Meaning)',
            style: TextStyle(fontSize: 16, color: Colors.grey, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 12),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16),
            child: Text(
              widget.word.meaning.isEmpty ? '[의미 없음]' : widget.word.meaning,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );
  }
}
