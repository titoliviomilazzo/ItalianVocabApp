# Project Status & Development History

**Last Updated:** 2026-02-10

## Project Overview
**ItalianVocabApp (Italiano 2000)** is a Flutter-based mobile application designed to help users learn the 2,000 most common Italian words. The app features a clean UI, level-based categorization, and a unique "4-panel comic story" approach to explain word meanings visually.

## Current State
- **Framework:** Flutter (Dark Mode supported theme)
- **Data Source:** `vocab.json` (7,200+ words derived from `Nuovo Vocabolario di Base`)
- **Assets:** Images stored in `assets/images/` (currently placeholders or generated via AI)

## Recent Accomplishments
1.  **Data Processing:**
    - Converted CSV data to JSON.
    -Enriched the first 100 words (Batch 1) with Korean meanings and 4-panel comic stories using AI.
2.  **Prompt Engineering:**
    - Developed a robust prompt generation script (`scripts/generate_prompts.py`) that creates 4-panel comic strip prompts for Genspark/Midjourney.
    - Validated styles (V1-V7) and settled on "European 2D comic book style".
    - Generated `genspark_prompts_batch1.txt` for the first 100 words.
3.  **UI Development:**
    - **HomeScreen:** Displays the vocabulary list with level indicators.
    - **FlashcardScreen:** Implemented a swipeable PageView for flashcards.
    - **FlashcardWidget:** Features flip animation (Front: Word/Image, Back: Meaning/Story).
    - **Navigation:** seamless transition from Home to Flashcards.
4.  **Debugging:**
    - Fixed `flutter run` issues by using external terminals and cleaning cache.
    - Implemented error handling for missing images.

## Next Steps (To-Do)
1.  **Image Generation:**
    - User to generate images for Batch 1 using `genspark_prompts_batch1.txt`.
    - Save images as `word_id.webp` in `assets/images/`.
2.  **Data Enrichment (Batch 2+):**
    - Run scripts to generate meanings/stories for the remaining ~7,100 words.
    - Update `vocab.json`.
3.  **UI Enhancements:**
    - Implement filtering by difficulty level (Fondamentale, Alto Uso, etc.).
    - Add "mark as learned" functionality.
    - Optimize asset loading for performance.
4.  **Deployment:**
    - Verify on physical devices (Android/iOS).

## Key Files
- `lib/main.dart`: Entry point.
- `lib/screens/home_screen.dart`: Main list view.
- `lib/screens/flashcard_screen.dart`: Flashcard container with swiping.
- `lib/widgets/flashcard_widget.dart`: Individual card UI logic.
- `scripts/enrich_util.py`: Utility for updating JSON data.
- `scripts/generate_prompts.py`: Prompt generation logic.
