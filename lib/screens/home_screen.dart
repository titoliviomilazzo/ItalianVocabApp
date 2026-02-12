import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/word.dart';
import '../screens/flashcard_screen.dart';
import '../screens/quiz_screen.dart';
import '../screens/stats_screen.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';

class HomeScreen extends StatefulWidget {
  final List<Word> words;

  const HomeScreen({super.key, required this.words});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late List<Word> _allWords;
  late List<Word> _filteredWords;
  String _selectedLevel = 'All';
  bool _hideLearned = false;
  String _searchQuery = '';
  final StorageService _storage = StorageService();
  final TextEditingController _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _allWords = widget.words;
    _filterWords();
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  void _filterWords() {
    setState(() {
      _filteredWords = _allWords.where((word) {
        final matchesLevel = _selectedLevel == 'All' || word.level == _selectedLevel;
        final matchesLearned = !_hideLearned || !word.isLearned;
        final matchesSearch = _searchQuery.isEmpty ||
            word.word.toLowerCase().contains(_searchQuery.toLowerCase()) ||
            word.meaning.toLowerCase().contains(_searchQuery.toLowerCase());
        return matchesLevel && matchesLearned && matchesSearch;
      }).toList();
    });
  }

  Future<void> _toggleLearned(int wordId) async {
    final index = _allWords.indexWhere((w) => w.id == wordId);
    if (index != -1) {
      final word = _allWords[index];
      final newStatus = !word.isLearned;
      
      if (newStatus) {
        await _storage.saveLearnedWord(wordId);
      } else {
        await _storage.removeLearnedWord(wordId);
      }

      setState(() {
        _allWords[index] = word.copyWith(isLearned: newStatus);
        _filterWords();
      });
    }
  }

  void _startQuiz() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => QuizScreen(words: _filteredWords),
      ),
    );
  }

  void _openStats() {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => StatsScreen(words: _allWords),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final learnedCount = _allWords.where((w) => w.isLearned).length;

    return Scaffold(
      body: CustomScrollView(
        slivers: [
          // ── Gradient AppBar ──
          SliverAppBar(
            expandedHeight: 120,
            floating: true,
            pinned: true,
            flexibleSpace: Container(
              decoration: const BoxDecoration(gradient: AppTheme.appBarGradient),
              child: FlexibleSpaceBar(
                title: Text(
                  'Dammi Parole',
                  style: GoogleFonts.outfit(
                    fontWeight: FontWeight.bold,
                    fontSize: 22,
                    color: Colors.white,
                    letterSpacing: 0.5,
                  ),
                ),
                titlePadding: const EdgeInsets.only(left: 16, bottom: 14),
              ),
            ),
            actions: [
              IconButton(
                icon: const Icon(Icons.bar_chart_rounded, color: Colors.white70),
                tooltip: '학습 통계',
                onPressed: _openStats,
              ),
              IconButton(
                icon: const Icon(Icons.quiz, color: Colors.white70),
                tooltip: '퀴즈 모드',
                onPressed: _startQuiz,
              ),
              PopupMenuButton<String>(
                icon: const Icon(Icons.filter_list, color: Colors.white70),
                onSelected: (value) {
                  if (value == 'Hide Learned') {
                    setState(() {
                       _hideLearned = !_hideLearned;
                       _filterWords();
                    });
                  } else {
                    setState(() {
                      _selectedLevel = value;
                      _filterWords();
                    });
                  }
                },
                itemBuilder: (context) => [
                  CheckedPopupMenuItem(
                    checked: _hideLearned,
                    value: 'Hide Learned',
                    child: const Text('학습 완료 숨기기'),
                  ),
                  const PopupMenuDivider(),
                  ...['All', 'Fondamentale', 'Alto Uso', 'Alta Disponibilità'].map((level) => 
                    CheckedPopupMenuItem(
                      checked: _selectedLevel == level,
                      value: level,
                      child: Text(level),
                    ),
                  ),
                ],
              ),
            ],
          ),

          // ── Progress bar ──
          SliverToBoxAdapter(
            child: Container(
              margin: const EdgeInsets.fromLTRB(16, 12, 16, 0),
              padding: const EdgeInsets.all(14),
              decoration: AppTheme.listTileDecoration,
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        '학습 진행률',
                        style: GoogleFonts.inter(
                          fontSize: 13,
                          fontWeight: FontWeight.w600,
                          color: AppTheme.warmGrey,
                        ),
                      ),
                      Text(
                        '$learnedCount / ${_allWords.length}',
                        style: GoogleFonts.inter(
                          fontSize: 13,
                          fontWeight: FontWeight.bold,
                          color: AppTheme.terracotta,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  ClipRRect(
                    borderRadius: BorderRadius.circular(6),
                    child: LinearProgressIndicator(
                      value: _allWords.isEmpty ? 0 : learnedCount / _allWords.length,
                      backgroundColor: AppTheme.lightTerracotta,
                      color: AppTheme.terracotta,
                      minHeight: 6,
                    ),
                  ),
                ],
              ),
            ),
          ),

          // ── Search bar ──
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 12, 16, 4),
              child: TextField(
                controller: _searchController,
                decoration: InputDecoration(
                  hintText: '단어 검색 (이탈리아어 / 한국어)',
                  hintStyle: TextStyle(color: AppTheme.warmGrey.withValues(alpha: 0.6)),
                  prefixIcon: const Icon(Icons.search, color: AppTheme.terracotta),
                  suffixIcon: _searchQuery.isNotEmpty
                      ? IconButton(
                          icon: const Icon(Icons.clear, size: 20, color: AppTheme.warmGrey),
                          onPressed: () {
                            _searchController.clear();
                            setState(() {
                              _searchQuery = '';
                              _filterWords();
                            });
                          },
                        )
                      : null,
                ),
                onChanged: (value) {
                  setState(() {
                    _searchQuery = value;
                    _filterWords();
                  });
                },
              ),
            ),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
              child: Text(
                '${_filteredWords.length}개 단어',
                style: TextStyle(color: AppTheme.warmGrey, fontSize: 13),
              ),
            ),
          ),

          // ── Word list ──
          SliverList(
            delegate: SliverChildBuilderDelegate(
              (context, index) {
                final word = _filteredWords[index];
                return Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 3),
                  child: Container(
                    decoration: AppTheme.listTileDecoration,
                    child: ListTile(
                      contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 2),
                      leading: Container(
                        width: 40,
                        height: 40,
                        decoration: BoxDecoration(
                          color: AppTheme.getLevelColor(word.level).withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(10),
                        ),
                        child: Center(
                          child: Text(
                            word.id.toString(),
                            style: TextStyle(
                              color: AppTheme.getLevelColor(word.level),
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                      ),
                      title: Text(
                        word.word, 
                        style: GoogleFonts.inter(
                          fontSize: 17, 
                          fontWeight: FontWeight.w600,
                          decoration: word.isLearned ? TextDecoration.lineThrough : null,
                          color: word.isLearned ? AppTheme.warmGrey : AppTheme.darkEspresso,
                        ),
                      ),
                      subtitle: Text(
                        word.meaning.isNotEmpty
                            ? '${word.gender} · ${word.meaning}'
                            : '${word.gender} · ${word.level}',
                        style: TextStyle(fontSize: 13, color: AppTheme.warmGrey),
                      ),
                      trailing: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          if (word.isLearned) 
                            const Icon(Icons.check_circle, color: AppTheme.oliveGreen, size: 20),
                          const SizedBox(width: 4),
                          Icon(Icons.arrow_forward_ios, size: 14, color: AppTheme.warmGrey.withValues(alpha: 0.5)),
                        ],
                      ),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => FlashcardScreen(
                              words: _filteredWords, 
                              initialIndex: index,
                              onToggleLearned: _toggleLearned,
                            ),
                          ),
                        );
                      },
                    ),
                  ),
                );
              },
              childCount: _filteredWords.length,
            ),
          ),
          const SliverToBoxAdapter(child: SizedBox(height: 80)),
        ],
      ),

      // ── Bottom action buttons ──
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          color: AppTheme.warmCream,
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.06),
              blurRadius: 10,
              offset: const Offset(0, -2),
            ),
          ],
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 10, 16, 10),
            child: Row(
              children: [
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: () {
                      if (_filteredWords.isEmpty) return;
                      showModalBottomSheet(
                        context: context,
                        shape: const RoundedRectangleBorder(
                          borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
                        ),
                        backgroundColor: AppTheme.warmCream,
                        builder: (ctx) => Padding(
                          padding: const EdgeInsets.fromLTRB(20, 20, 20, 30),
                          child: Column(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Container(
                                width: 40, height: 4,
                                decoration: BoxDecoration(
                                  color: AppTheme.warmGrey.withValues(alpha: 0.3),
                                  borderRadius: BorderRadius.circular(2),
                                ),
                              ),
                              const SizedBox(height: 20),
                              Text(
                                '학습 모드 선택',
                                style: GoogleFonts.outfit(
                                  fontSize: 20,
                                  fontWeight: FontWeight.bold,
                                  color: AppTheme.darkEspresso,
                                ),
                              ),
                              const SizedBox(height: 16),
                              _buildStudyOption(
                                ctx,
                                icon: Icons.format_list_numbered,
                                color: AppTheme.terracotta,
                                title: '순서대로 학습',
                                subtitle: '1번부터 차례대로',
                                onTap: () {
                                  Navigator.pop(ctx);
                                  Navigator.push(context, MaterialPageRoute(
                                    builder: (_) => FlashcardScreen(
                                      words: _filteredWords,
                                      initialIndex: 0,
                                      onToggleLearned: _toggleLearned,
                                    ),
                                  ));
                                },
                              ),
                              const SizedBox(height: 10),
                              _buildStudyOption(
                                ctx,
                                icon: Icons.shuffle,
                                color: AppTheme.goldenAmber,
                                title: '랜덤 셔플',
                                subtitle: '무작위 순서로 학습',
                                onTap: () {
                                  Navigator.pop(ctx);
                                  Navigator.push(context, MaterialPageRoute(
                                    builder: (_) => FlashcardScreen(
                                      words: _filteredWords,
                                      initialIndex: 0,
                                      onToggleLearned: _toggleLearned,
                                      shuffle: true,
                                    ),
                                  ));
                                },
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                    icon: const Icon(Icons.style),
                    label: Text('학습 시작', style: GoogleFonts.inter(fontSize: 15, fontWeight: FontWeight.bold)),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppTheme.terracotta,
                      foregroundColor: Colors.white,
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: _startQuiz,
                    icon: const Icon(Icons.quiz),
                    label: Text('퀴즈 도전', style: GoogleFonts.inter(fontSize: 15, fontWeight: FontWeight.bold)),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppTheme.deepWine,
                      foregroundColor: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildStudyOption(BuildContext ctx, {
    required IconData icon,
    required Color color,
    required String title,
    required String subtitle,
    required VoidCallback onTap,
  }) {
    return ListTile(
      leading: Container(
        width: 42, height: 42,
        decoration: BoxDecoration(
          color: color.withValues(alpha: 0.12),
          borderRadius: BorderRadius.circular(12),
        ),
        child: Icon(icon, color: color),
      ),
      title: Text(title, style: GoogleFonts.inter(fontWeight: FontWeight.w600)),
      subtitle: Text(subtitle, style: TextStyle(color: AppTheme.warmGrey, fontSize: 13)),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      tileColor: AppTheme.softWhite,
      onTap: onTap,
    );
  }
}
