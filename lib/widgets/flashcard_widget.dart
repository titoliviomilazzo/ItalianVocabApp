import 'package:flutter/material.dart';
import '../models/word.dart';

class FlashcardWidget extends StatefulWidget {
  final Word word;

  const FlashcardWidget({super.key, required this.word});

  @override
  State<FlashcardWidget> createState() => _FlashcardWidgetState();
}

class _FlashcardWidgetState extends State<FlashcardWidget> {
  bool isFront = true;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => setState(() => isFront = !isFront),
      child: Card(
        elevation: 8,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        child: Container(
          width: 300,
          height: 450,
          padding: const EdgeInsets.all(20),
          child: isFront ? _buildFront() : _buildBack(),
        ),
      ),
    );
  }

  Widget _buildFront() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Expanded(
          child: Container(
            width: double.infinity,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(15),
              color: Colors.grey[200],
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(15),
              child: Image.asset(
                widget.word.imagePath,
                fit: BoxFit.cover,
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
        const SizedBox(height: 20),
        Text(
          widget.word.word,
          style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
        ),
        Text(
          widget.word.gender,
          style: TextStyle(fontSize: 16, color: Colors.grey[600]),
        ),
      ],
    );
  }

  Widget _buildBack() {
    return SingleChildScrollView(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            '뜻 (Meaning)',
            style: TextStyle(fontSize: 16, color: Colors.grey, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 5),
          Text(
            widget.word.meaning.isEmpty ? '[의미 없음]' : widget.word.meaning,
            textAlign: TextAlign.center,
            style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          const Divider(height: 30),
          const Text(
            '4컷 만화 시나리오 (Story)',
            style: TextStyle(fontSize: 16, color: Colors.grey, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 10),
          Text(
            widget.word.story.isEmpty ? '[시나리오 없음]' : widget.word.story.replaceAll('. ', '.\n'),
            textAlign: TextAlign.left,
            style: const TextStyle(fontSize: 14, height: 1.4),
          ),
        ],
      ),
    );
  }
}
