import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/word.dart';
import '../theme/app_theme.dart';

class StatsScreen extends StatelessWidget {
  final List<Word> words;

  const StatsScreen({super.key, required this.words});

  @override
  Widget build(BuildContext context) {
    final totalWords = words.length;
    final learnedWords = words.where((w) => w.isLearned).length;
    final withMeaning = words.where((w) => w.meaning.isNotEmpty).length;
    final withImage = words.where((w) => !w.imagePath.endsWith('.webp')).length;
    final learnedPercent = totalWords > 0 ? (learnedWords / totalWords * 100) : 0.0;

    final levels = ['Fondamentale', 'Alto Uso', 'Alta Disponibilità'];
    final levelData = levels.map((level) {
      final total = words.where((w) => w.level == level).length;
      final learned = words.where((w) => w.level == level && w.isLearned).length;
      return _LevelStat(level, total, learned);
    }).toList();

    return Scaffold(
      backgroundColor: AppTheme.warmCream,
      appBar: AppBar(
        title: Text('학습 통계', style: GoogleFonts.outfit(fontWeight: FontWeight.bold)),
        flexibleSpace: Container(decoration: const BoxDecoration(gradient: AppTheme.appBarGradient)),
        foregroundColor: Colors.white,
        elevation: 0,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            // Overall progress card
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(28),
              decoration: AppTheme.cardDecoration,
              child: Column(
                children: [
                  Text(
                    '전체 학습 진행률',
                    style: GoogleFonts.inter(
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                      color: AppTheme.warmGrey,
                    ),
                  ),
                  const SizedBox(height: 24),
                  SizedBox(
                    width: 150,
                    height: 150,
                    child: Stack(
                      fit: StackFit.expand,
                      children: [
                        CircularProgressIndicator(
                          value: learnedPercent / 100,
                          strokeWidth: 12,
                          backgroundColor: AppTheme.lightTerracotta,
                          valueColor: const AlwaysStoppedAnimation<Color>(AppTheme.terracotta),
                          strokeCap: StrokeCap.round,
                        ),
                        Center(
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Text(
                                '${learnedPercent.round()}%',
                                style: GoogleFonts.outfit(
                                  fontSize: 36,
                                  fontWeight: FontWeight.bold,
                                  color: AppTheme.terracotta,
                                ),
                              ),
                              Text(
                                '$learnedWords / $totalWords',
                                style: GoogleFonts.inter(
                                  fontSize: 14,
                                  color: AppTheme.warmGrey,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            // Quick stats row
            Row(
              children: [
                _buildStatCard('📚 전체 단어', '$totalWords', AppTheme.terracotta),
                const SizedBox(width: 12),
                _buildStatCard('✅ 학습 완료', '$learnedWords', AppTheme.oliveGreen),
              ],
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                _buildStatCard('📝 뜻 보강', '$withMeaning', AppTheme.goldenAmber),
                const SizedBox(width: 12),
                _buildStatCard('🖼️ 이미지', '$withImage', AppTheme.altaDisponibilita),
              ],
            ),
            const SizedBox(height: 24),

            // Level breakdown
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: AppTheme.cardDecoration,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    '레벨별 진행률',
                    style: GoogleFonts.inter(
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                      color: AppTheme.warmGrey,
                    ),
                  ),
                  const SizedBox(height: 20),
                  ...levelData.map((stat) => Padding(
                    padding: const EdgeInsets.only(bottom: 18),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Row(
                              children: [
                                Container(
                                  width: 12,
                                  height: 12,
                                  decoration: BoxDecoration(
                                    color: AppTheme.getLevelColor(stat.level),
                                    borderRadius: BorderRadius.circular(3),
                                  ),
                                ),
                                const SizedBox(width: 8),
                                Text(
                                  stat.level,
                                  style: GoogleFonts.inter(
                                    fontSize: 14,
                                    fontWeight: FontWeight.w500,
                                    color: AppTheme.darkEspresso,
                                  ),
                                ),
                              ],
                            ),
                            Text(
                              '${stat.learned} / ${stat.total}',
                              style: GoogleFonts.inter(
                                fontSize: 13,
                                color: AppTheme.warmGrey,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(6),
                          child: LinearProgressIndicator(
                            value: stat.total > 0 ? stat.learned / stat.total : 0,
                            minHeight: 8,
                            backgroundColor: AppTheme.lightTerracotta,
                            valueColor: AlwaysStoppedAnimation<Color>(
                              AppTheme.getLevelColor(stat.level),
                            ),
                          ),
                        ),
                      ],
                    ),
                  )),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStatCard(String label, String value, Color color) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 18, horizontal: 12),
        decoration: BoxDecoration(
          color: AppTheme.softWhite,
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.04),
              blurRadius: 8,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        child: Column(
          children: [
            Text(
              value,
              style: GoogleFonts.outfit(
                fontSize: 28,
                fontWeight: FontWeight.bold,
                color: color,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              label,
              style: GoogleFonts.inter(
                fontSize: 13,
                color: AppTheme.warmGrey,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _LevelStat {
  final String level;
  final int total;
  final int learned;
  _LevelStat(this.level, this.total, this.learned);
}
