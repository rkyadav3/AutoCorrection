# AutoCorrection Project

This project is a **real-time Auto-Correction Tool** that listens to keyboard inputs, identifies misspelled words, and replaces them with the correct spelling automatically. It leverages Python libraries to detect and correct spelling mistakes on the fly while typing.

---

## Features

- Monitors keyboard input in real-time.
- Automatically corrects misspelled words upon pressing the spacebar.
- Simulates backspace to remove the incorrect word and replaces it with the corrected word.
- Provides seamless integration with any text input field or editor.

---

## How It Works

1. **Keyboard Monitoring**:
   - The `pynput` library is used to capture keyboard events.
   
2. **Spell Checking**:
   - The `SpellChecker` library identifies and suggests corrections for misspelled words.
   
3. **Auto-Correction**:
   - The `pyautogui` library simulates typing actions (backspace and corrected text) to replace misspelled words.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/AutoCorrection.git
   cd AutoCorrection
2. Install the required dependencies:
   ```bash
   pip install pynput pyautogui pyspellchecker
3. Run the script:
   ```bash
   python autocorrection.py
##Usage
  -Start the script.
  -Begin typing in any text input field.
  -Misspelled words will be auto-corrected as you type when the spacebar is pressed.
##Requirements
  -Python 3.x
##Libraries:
  -pynput
  -pyautogui
  -pyspellchecker
#Limitations
  -May not work properly with non-standard keyboard layouts.
  -Requires focus on the text field to function correctly.
  -Works only for single-word corrections; compound corrections are not supported.
#Contributions
  -Feel free to contribute by:

#Forking this repository.
  -Creating a new branch for your feature or fix.
  -Submitting a pull request.
#License
This project is open-source and available under the MIT License.
