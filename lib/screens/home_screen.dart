import 'package:flutter/material.dart';
import '../models/word.dart';
import '../screens/flashcard_screen.dart';

class HomeScreen extends StatelessWidget {
  final List<Word> words;

  const HomeScreen({super.key, required this.words});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Italiano 2000', style: TextStyle(fontWeight: FontWeight.bold)),
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
      ),
      body: ListView.builder(
        itemCount: words.length > 100 ? 100 : words.length, // Preview first 100 (Batch 1)
        itemBuilder: (context, index) {
          final word = words[index];
          return ListTile(
            leading: CircleAvatar(
              backgroundColor: _getLevelColor(word.level),
              child: Text(word.id.toString(), style: const TextStyle(color: Colors.white, fontSize: 12)),
            ),
            title: Text(word.word, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            subtitle: Text('${word.gender} • ${word.level}'),
            trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => FlashcardScreen(words: words, initialIndex: index),
                ),
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => FlashcardScreen(words: words, initialIndex: 0),
            ),
          );
        },
        label: const Text('학습 시작'),
        icon: const Icon(Icons.play_arrow),
        backgroundColor: Colors.indigo,
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
