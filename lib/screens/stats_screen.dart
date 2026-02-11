import 'package:flutter/material.dart';
import '../models/word.dart';

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

    // Level breakdown
    final levels = ['Fondamentale', 'Alto Uso', 'Alta Disponibilità'];
    final levelData = levels.map((level) {
      final total = words.where((w) => w.level == level).length;
      final learned = words.where((w) => w.level == level && w.isLearned).length;
      return _LevelStat(level, total, learned);
    }).toList();

    return Scaffold(
      appBar: AppBar(
        title: const Text('학습 통계'),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            // Overall progress card
            Card(
              elevation: 4,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(
                  children: [
                    const Text(
                      '전체 학습 진행률',
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black54),
                    ),
                    const SizedBox(height: 20),
                    SizedBox(
                      width: 150,
                      height: 150,
                      child: Stack(
                        fit: StackFit.expand,
                        children: [
                          CircularProgressIndicator(
                            value: learnedPercent / 100,
                            strokeWidth: 12,
                            backgroundColor: Colors.grey[200],
                            valueColor: const AlwaysStoppedAnimation<Color>(Colors.indigo),
                          ),
                          Center(
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  '${learnedPercent.round()}%',
                                  style: const TextStyle(
                                    fontSize: 36,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.indigo,
                                  ),
                                ),
                                Text(
                                  '$learnedWords / $totalWords',
                                  style: TextStyle(fontSize: 14, color: Colors.grey[600]),
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
            ),
            const SizedBox(height: 20),

            // Quick stats row
            Row(
              children: [
                _buildStatCard('📚 전체 단어', '$totalWords', Colors.indigo),
                const SizedBox(width: 12),
                _buildStatCard('✅ 학습 완료', '$learnedWords', Colors.green),
              ],
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                _buildStatCard('📝 뜻 보강', '$withMeaning', Colors.orange),
                const SizedBox(width: 12),
                _buildStatCard('🖼️ 이미지', '$withImage', Colors.blue),
              ],
            ),
            const SizedBox(height: 24),

            // Level breakdown
            Card(
              elevation: 4,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      '레벨별 진행률',
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black54),
                    ),
                    const SizedBox(height: 16),
                    ...levelData.map((stat) => Padding(
                      padding: const EdgeInsets.only(bottom: 16),
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
                                      color: _getLevelColor(stat.level),
                                      borderRadius: BorderRadius.circular(3),
                                    ),
                                  ),
                                  const SizedBox(width: 8),
                                  Text(
                                    stat.level,
                                    style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w500),
                                  ),
                                ],
                              ),
                              Text(
                                '${stat.learned} / ${stat.total}',
                                style: TextStyle(fontSize: 14, color: Colors.grey[600]),
                              ),
                            ],
                          ),
                          const SizedBox(height: 6),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(6),
                            child: LinearProgressIndicator(
                              value: stat.total > 0 ? stat.learned / stat.total : 0,
                              minHeight: 10,
                              backgroundColor: Colors.grey[200],
                              valueColor: AlwaysStoppedAnimation<Color>(_getLevelColor(stat.level)),
                            ),
                          ),
                        ],
                      ),
                    )),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStatCard(String label, String value, Color color) {
    return Expanded(
      child: Card(
        elevation: 2,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 12),
          child: Column(
            children: [
              Text(
                value,
                style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: color),
              ),
              const SizedBox(height: 4),
              Text(
                label,
                style: TextStyle(fontSize: 13, color: Colors.grey[600]),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Color _getLevelColor(String level) {
    switch (level) {
      case 'Fondamentale': return Colors.green;
      case 'Alto Uso': return Colors.orange;
      case 'Alta Disponibilità': return Colors.blue;
      default: return Colors.grey;
    }
  }
}

class _LevelStat {
  final String level;
  final int total;
  final int learned;
  _LevelStat(this.level, this.total, this.learned);
}
