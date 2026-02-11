import 'package:flutter/material.dart';
import '../models/word.dart';
import '../screens/flashcard_screen.dart';
import '../screens/quiz_screen.dart';
import '../screens/stats_screen.dart';
import '../services/storage_service.dart';

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
    return Scaffold(
      appBar: AppBar(
        title: const Text('Italiano 2000', style: TextStyle(fontWeight: FontWeight.bold)),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
        actions: [
          IconButton(
            icon: const Icon(Icons.bar_chart_rounded),
            tooltip: '학습 통계',
            onPressed: _openStats,
          ),
          IconButton(
            icon: const Icon(Icons.quiz),
            tooltip: '퀴즈 모드',
            onPressed: _startQuiz,
          ),
          PopupMenuButton<String>(
            icon: const Icon(Icons.filter_list),
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
                child: const Text('Hide Learned'),
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
      body: Column(
        children: [
          // Search bar
          Padding(
            padding: const EdgeInsets.fromLTRB(12, 10, 12, 4),
            child: TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: '단어 검색 (이탈리아어 / 한국어)',
                prefixIcon: const Icon(Icons.search, color: Colors.indigo),
                suffixIcon: _searchQuery.isNotEmpty
                    ? IconButton(
                        icon: const Icon(Icons.clear, size: 20),
                        onPressed: () {
                          _searchController.clear();
                          setState(() {
                            _searchQuery = '';
                            _filterWords();
                          });
                        },
                      )
                    : null,
                filled: true,
                fillColor: Colors.grey[100],
                contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 16),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: BorderSide.none,
                ),
                focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: const BorderSide(color: Colors.indigo, width: 1.5),
                ),
              ),
              onChanged: (value) {
                setState(() {
                  _searchQuery = value;
                  _filterWords();
                });
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
            child: Text(
              '${_filteredWords.length}개 단어',
              style: TextStyle(color: Colors.grey[600], fontSize: 13),
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: _filteredWords.length > 100 ? 100 : _filteredWords.length,
              itemBuilder: (context, index) {
                final word = _filteredWords[index];
                return ListTile(
                  leading: CircleAvatar(
                    backgroundColor: _getLevelColor(word.level),
                    child: Text(word.id.toString(), style: const TextStyle(color: Colors.white, fontSize: 12)),
                  ),
                  title: Text(
                    word.word, 
                    style: TextStyle(
                      fontSize: 18, 
                      fontWeight: FontWeight.bold,
                      decoration: word.isLearned ? TextDecoration.lineThrough : null,
                      color: word.isLearned ? Colors.grey : Colors.black,
                    ),
                  ),
                  subtitle: Text(
                    word.meaning.isNotEmpty
                        ? '${word.gender} • ${word.meaning}'
                        : '${word.gender} • ${word.level}',
                  ),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      if (word.isLearned) 
                        const Icon(Icons.check_circle, color: Colors.green, size: 20),
                      const SizedBox(width: 8),
                      const Icon(Icons.arrow_forward_ios, size: 16),
                    ],
                  ),
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
                );
              },
            ),
          ),
        ],
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
        child: Row(
          children: [
            Expanded(
              child: ElevatedButton.icon(
                onPressed: () {
                  if (_filteredWords.isEmpty) return;
                  showModalBottomSheet(
                    context: context,
                    shape: const RoundedRectangleBorder(
                      borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
                    ),
                    builder: (ctx) => Padding(
                      padding: const EdgeInsets.fromLTRB(20, 20, 20, 30),
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Text('학습 모드 선택', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                          const SizedBox(height: 16),
                          ListTile(
                            leading: const Icon(Icons.format_list_numbered, color: Colors.indigo),
                            title: const Text('순서대로 학습'),
                            subtitle: const Text('1번부터 차례대로'),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                            tileColor: Colors.indigo.withValues(alpha: 0.05),
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
                          ListTile(
                            leading: const Icon(Icons.shuffle, color: Colors.deepOrange),
                            title: const Text('🔀 랜덤 셔플'),
                            subtitle: const Text('무작위 순서로 학습'),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                            tileColor: Colors.deepOrange.withValues(alpha: 0.05),
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
                label: const Text('학습 시작', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.indigo,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                ),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: ElevatedButton.icon(
                onPressed: _startQuiz,
                icon: const Icon(Icons.quiz),
                label: const Text('퀴즈 도전', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.deepOrange,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                ),
              ),
            ),
          ],
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

