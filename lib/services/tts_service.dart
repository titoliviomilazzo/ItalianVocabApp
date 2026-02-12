import 'package:web/web.dart' as web;

class TtsService {
  static void speak(String text, {String lang = 'it-IT'}) {
    web.window.speechSynthesis.cancel();
    final utterance = web.SpeechSynthesisUtterance(text);
    utterance.lang = lang;
    utterance.rate = 0.85;
    web.window.speechSynthesis.speak(utterance);
  }

  static void stop() {
    web.window.speechSynthesis.cancel();
  }
}
