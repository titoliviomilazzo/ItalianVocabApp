class Word {
  final int id;
  final String word;
  final String gender;
  final String level;
  final String meaning;
  final String pronunciation;
  final String story;
  final String imagePath;
  final String example;
  final bool isLearned;

  Word({
    required this.id,
    required this.word,
    required this.gender,
    required this.level,
    required this.meaning,
    required this.pronunciation,
    required this.imagePath,
    required this.story,
    this.example = '',
    this.isLearned = false,
  });

  factory Word.fromJson(Map<String, dynamic> json, {bool isLearned = false}) {
    return Word(
      id: json['id'] as int,
      word: json['word'] as String,
      gender: json['gender'] as String,
      level: json['level'] as String,
      meaning: json['meaning'] as String,
      pronunciation: json['pronunciation'] as String,
      imagePath: json['image_path'] as String,
      story: json['story'] as String? ?? "",
      example: json['example'] as String? ?? "",
      isLearned: isLearned,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'word': word,
      'gender': gender,
      'level': level,
      'meaning': meaning,
      'pronunciation': pronunciation,
      'image_path': imagePath,
      'story': story,
      'example': example,
      'isLearned': isLearned,
    };
  }
  
  Word copyWith({bool? isLearned}) {
    return Word(
      id: id,
      word: word,
      gender: gender,
      level: level,
      meaning: meaning,
      pronunciation: pronunciation,
      imagePath: imagePath,
      story: story,
      example: example,
      isLearned: isLearned ?? this.isLearned,
    );
  }
}

