import 'dart:js_interop';
import 'package:web/web.dart' as web;

class TtsService {
  static void speak(String text, {String lang = 'it-IT'}) {
    // Cancel any ongoing speech
    web.window.speechSynthesis.cancel();

    final utterance = web.SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    utterance.rate = 0.85; // Slightly slow for learners
    utterance.pitch = 1.0;
    utterance.volume = 1.0;

    web.window.speechSynthesis.speak(utterance);
  }

  static void stop() {
    web.window.speechSynthesis.cancel();
  }
}
