import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import 'models/word.dart';
import 'screens/home_screen.dart';
import 'services/storage_service.dart';
import 'theme/app_theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dammi Parole',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme.copyWith(
        textTheme: GoogleFonts.interTextTheme(
          AppTheme.lightTheme.textTheme,
        ),
      ),
      home: const DataLoadingWrapper(),
    );
  }
}

class DataLoadingWrapper extends StatefulWidget {
  const DataLoadingWrapper({super.key});

  @override
  State<DataLoadingWrapper> createState() => _DataLoadingWrapperState();
}

class _DataLoadingWrapperState extends State<DataLoadingWrapper> {
  late Future<List<Word>> _wordsFuture;

  @override
  void initState() {
    super.initState();
    _wordsFuture = _loadWords();
  }

  Future<List<Word>> _loadWords() async {
    try {
      final String response = await rootBundle.loadString('assets/data/vocab.json');
      final List<dynamic> data = json.decode(response);
      final storage = StorageService();
      final learnedIds = await storage.getLearnedWords();
      
      return data.map((json) {
        final word = Word.fromJson(json);
        return word.copyWith(isLearned: learnedIds.contains(word.id));
      }).toList();
    } catch (e) {
      debugPrint('Error loading vocab.json: $e');
      rethrow;
    }
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<Word>>(
      future: _wordsFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return Scaffold(
            backgroundColor: AppTheme.warmCream,
            body: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    'Dammi Parole',
                    style: GoogleFonts.outfit(
                      fontSize: 32,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.terracotta,
                    ),
                  ),
                  const SizedBox(height: 24),
                  const CircularProgressIndicator(color: AppTheme.terracotta),
                ],
              ),
            ),
          );
        } else if (snapshot.hasError) {
          return Scaffold(
            body: Center(
              child: Padding(
                padding: const EdgeInsets.all(20.0),
                child: Text('Error loading data: ${snapshot.error}\n\nMake sure assets/data/vocab.json exists and is valid.'),
              ),
            ),
          );
        } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
          return const Scaffold(
            body: Center(child: Text('No data found in vocab.json')),
          );
        } else {
          return HomeScreen(words: snapshot.data!);
        }
      },
    );
  }
}
