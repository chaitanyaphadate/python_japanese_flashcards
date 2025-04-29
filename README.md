# 🈶 Japanese Flashcards App

A simple, interactive flashcard application built using Python and Tkinter to help users learn and remember Japanese vocabulary. The app shows a Japanese word (Hiragana) and, upon flipping the card, reveals its English meaning and pronunciation. Users can track their learning progress visually.

---

## 📸 Screenshots

*Add screenshots of the app here (e.g., flashcard front, back, UI interface).*

---

## 🚀 Features

- 📚 Flashcard-style learning interface for Japanese Hiragana vocabulary  
- 🔁 Flip cards to view English meaning and pronunciation  
- ✅ Track correct guesses using visual tick marks (`✔`)  
- 📝 Automatically saves your progress (words you’ve learned) to `words_to_learn.csv`  
- 🎨 Clean and intuitive GUI built using Tkinter  
- 🎯 Keyboard shortcuts for ease of use:
  - Press **A**: Mark as wrong  
  - Press **S**: Flip the card  
  - Press **D**: Mark as correct  

---

## 🛠 Tech Stack

- **Python 3**
- **Tkinter** – for GUI
- **Pandas** – for data handling

---

## 📂 Project Structure

```text
├── data/
│   ├── japanese_vocab.csv         # Master vocabulary file
│   └── words_to_learn.csv         # Progress tracking file (created automatically)
├── images/
│   ├── card_front.png             # Image used for flashcard front
│   ├── card_back.png              # Image used for flashcard back
│   ├── right.png                  # Tick mark image
│   ├── wrong.png                  # Cross image
│   └── flip_card.png              # Flip button image
├── main.py                        # Main application script
```
---

## 🔮 Future Enhancements
- Add sound/pronunciation for better learning

- Add support for Kanji 

- Add progress stats dashboard

- Export learned words as PDF or CSV

---

## 👨‍💻 Author
Chaitanya
