
class TtsService {
  static void speak(String text, {String lang = 'it-IT'}) {
    // TTS disabled temporarily to fix deployment
    print('TTS: $text');
  }

  static void stop() {}
}
