import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/word.dart';
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
      _isFront = true;
      _controller.reset();
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
          // ── Image area ──
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
                child: Image.asset(
                  widget.word.imagePath,
                  fit: BoxFit.contain,
                  errorBuilder: (context, error, stackTrace) {
                    return Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.image_not_supported, size: 48, color: AppTheme.warmGrey.withValues(alpha: 0.5)),
                        const SizedBox(height: 10),
                        Text(
                          'Immagine non disponibile',
                          style: GoogleFonts.inter(color: AppTheme.warmGrey, fontSize: 13),
                        ),
                      ],
                    );
                  },
                ),
              ),
            ),
          ),
          const SizedBox(height: 16),

          // ── Word + TTS ──
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

          // ── Tap hint ──
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.touch_app, size: 14, color: AppTheme.warmGrey.withValues(alpha: 0.4)),
              const SizedBox(width: 4),
              Text(
                '탭하여 뒤집기',
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
            // ── Word header with TTS ──
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

            // ── Divider ──
            Container(
              width: 40,
              height: 3,
              decoration: BoxDecoration(
                gradient: AppTheme.accentGradient,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: 20),

            // ── Meaning ──
            _buildSection(
              label: '뜻',
              icon: Icons.translate,
              child: Text(
                widget.word.meaning.isEmpty ? '(의미 없음)' : widget.word.meaning,
                textAlign: TextAlign.center,
                style: GoogleFonts.inter(
                  fontSize: 26,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.darkEspresso,
                ),
              ),
            ),

            // ── Story ──
            if (widget.word.story.isNotEmpty) ...[
              const SizedBox(height: 20),
              _buildSection(
                label: 'Story',
                icon: Icons.auto_stories,
                child: Text(
                  widget.word.story,
                  textAlign: TextAlign.center,
                  style: GoogleFonts.inter(
                    fontSize: 14,
                    color: AppTheme.darkEspresso.withValues(alpha: 0.8),
                    height: 1.6,
                  ),
                ),
              ),
            ],

            // ── Example sentence ──
            if (widget.word.example.isNotEmpty) ...[
              const SizedBox(height: 20),
              _buildSection(
                label: 'Esempio',
                icon: Icons.format_quote,
                child: Text(
                  widget.word.example,
                  textAlign: TextAlign.center,
                  style: GoogleFonts.inter(
                    fontSize: 15,
                    color: AppTheme.deepWine,
                    fontStyle: FontStyle.italic,
                    height: 1.5,
                  ),
                ),
              ),
            ],

            const SizedBox(height: 20),

            // ── Tap hint ──
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.touch_app, size: 14, color: AppTheme.warmGrey.withValues(alpha: 0.4)),
                const SizedBox(width: 4),
                Text(
                  '탭하여 앞면으로',
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
        border: Border.all(
          color: AppTheme.terracotta.withValues(alpha: 0.08),
        ),
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
}
