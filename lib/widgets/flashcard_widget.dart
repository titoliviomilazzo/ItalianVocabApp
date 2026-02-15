import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/word.dart';
import '../services/asset_image_service.dart';
import '../services/tts_service.dart';
import '../theme/app_theme.dart';

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
  late Future<String?> _resolvedImageFuture;
  bool _isFront = true;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 400),
      vsync: this,
    );
    _animation = Tween<double>(
      begin: 0,
      end: 1,
    ).animate(CurvedAnimation(parent: _controller, curve: Curves.easeInOut));
    _resolvedImageFuture = AssetImageService.resolveWordImagePath(widget.word);
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
      _isFront = true;
      _controller.reset();
      _resolvedImageFuture = AssetImageService.resolveWordImagePath(
        widget.word,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;
    final screenHeight = MediaQuery.of(context).size.height;
    final cardWidth = screenWidth * 0.88 > 420 ? 420.0 : screenWidth * 0.88;
    final cardHeight = screenHeight * 0.72;

    return GestureDetector(
      onTap: _flipCard,
      child: AnimatedBuilder(
        animation: _animation,
        builder: (context, child) {
          double angle;
          final bool showFront = _animation.value < 0.5;
          if (_animation.value <= 0.5) {
            angle = _animation.value * pi;
          } else {
            angle = (_animation.value - 1) * pi;
          }
          final transform = Matrix4.identity()
            ..setEntry(3, 2, 0.001)
            ..rotateY(angle);

          return Transform(
            alignment: Alignment.center,
            transform: transform,
            child: Container(
              width: cardWidth,
              height: cardHeight,
              decoration: AppTheme.cardDecoration,
              child: ClipRRect(
                borderRadius: BorderRadius.circular(24),
                child: showFront ? _buildFront() : _buildBack(),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildFront() {
    return Container(
      padding: const EdgeInsets.all(16),
      child: Column(
        children: [
          Expanded(
            flex: 5,
            child: Container(
              width: double.infinity,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                color: AppTheme.lightTerracotta.withValues(alpha: 0.5),
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: FutureBuilder<String?>(
                  future: _resolvedImageFuture,
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return const Center(
                        child: CircularProgressIndicator(
                          color: AppTheme.terracotta,
                        ),
                      );
                    }

                    final resolvedPath = snapshot.data;
                    if (resolvedPath == null || resolvedPath.isEmpty) {
                      return _buildImageUnavailable();
                    }

                    return Image.asset(
                      resolvedPath,
                      fit: BoxFit.contain,
                      errorBuilder: (context, error, stackTrace) =>
                          _buildImageUnavailable(),
                    );
                  },
                ),
              ),
            ),
          ),
          const SizedBox(height: 16),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Flexible(
                child: Text(
                  widget.word.word,
                  style: GoogleFonts.outfit(
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                    color: AppTheme.darkEspresso,
                  ),
                  overflow: TextOverflow.ellipsis,
                ),
              ),
              const SizedBox(width: 10),
              GestureDetector(
                onTap: () => TtsService.speak(widget.word.word),
                child: Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: AppTheme.terracotta.withValues(alpha: 0.1),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Icon(
                    Icons.volume_up_rounded,
                    size: 22,
                    color: AppTheme.terracotta,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          Text(
            widget.word.gender,
            style: GoogleFonts.inter(
              fontSize: 14,
              color: AppTheme.warmGrey,
              fontStyle: FontStyle.italic,
            ),
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                Icons.touch_app,
                size: 14,
                color: AppTheme.warmGrey.withValues(alpha: 0.4),
              ),
              const SizedBox(width: 4),
              Text(
                'Tap to flip',
                style: GoogleFonts.inter(
                  fontSize: 11,
                  color: AppTheme.warmGrey.withValues(alpha: 0.4),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildBack() {
    return Container(
      padding: const EdgeInsets.all(20),
      child: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Flexible(
                  child: Text(
                    widget.word.word,
                    style: GoogleFonts.outfit(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.terracotta,
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                GestureDetector(
                  onTap: () => TtsService.speak(widget.word.word),
                  child: Icon(
                    Icons.volume_up_rounded,
                    size: 20,
                    color: AppTheme.terracotta.withValues(alpha: 0.6),
                  ),
                ),
              ],
            ),
            Text(
              widget.word.gender,
              style: GoogleFonts.inter(
                fontSize: 13,
                color: AppTheme.warmGrey,
                fontStyle: FontStyle.italic,
              ),
            ),
            const SizedBox(height: 16),
            Container(
              width: 40,
              height: 3,
              decoration: BoxDecoration(
                gradient: AppTheme.accentGradient,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: 20),
            _buildSection(
              label: 'Meaning',
              icon: Icons.translate,
              child: Text(
                widget.word.meaning.isEmpty
                    ? '(meaning not available)'
                    : widget.word.meaning,
                textAlign: TextAlign.center,
                style: GoogleFonts.inter(
                  fontSize: 26,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.darkEspresso,
                ),
              ),
            ),
            const SizedBox(height: 20),
            _buildSection(
              label: 'Esempio',
              icon: Icons.format_quote,
              child: Text(
                _displayExample(widget.word),
                textAlign: TextAlign.center,
                style: GoogleFonts.inter(
                  fontSize: 15,
                  color: AppTheme.deepWine,
                  fontStyle: FontStyle.italic,
                  height: 1.5,
                ),
              ),
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.touch_app,
                  size: 14,
                  color: AppTheme.warmGrey.withValues(alpha: 0.4),
                ),
                const SizedBox(width: 4),
                Text(
                  'Tap to return',
                  style: GoogleFonts.inter(
                    fontSize: 11,
                    color: AppTheme.warmGrey.withValues(alpha: 0.4),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSection({
    required String label,
    required IconData icon,
    required Widget child,
  }) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: AppTheme.softWhite.withValues(alpha: 0.7),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppTheme.terracotta.withValues(alpha: 0.08)),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(icon, size: 14, color: AppTheme.warmGrey),
              const SizedBox(width: 4),
              Text(
                label,
                style: GoogleFonts.inter(
                  fontSize: 12,
                  fontWeight: FontWeight.w600,
                  color: AppTheme.warmGrey,
                  letterSpacing: 0.5,
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          child,
        ],
      ),
    );
  }

  String _displayExample(Word word) {
    final example = word.example.trim();
    if (example.isNotEmpty) return example;
    return "Esempio: '${word.word}' in una frase.";
  }

  Widget _buildImageUnavailable() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Icon(
          Icons.image_not_supported,
          size: 48,
          color: AppTheme.warmGrey.withValues(alpha: 0.5),
        ),
        const SizedBox(height: 10),
        Text(
          'Immagine non disponibile',
          style: GoogleFonts.inter(color: AppTheme.warmGrey, fontSize: 13),
        ),
      ],
    );
  }
}
