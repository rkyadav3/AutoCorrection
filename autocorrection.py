import pynput
from pynput.keyboard import Key, Listener
import pyautogui
from spellchecker import SpellChecker

# Initialize spell checker
spell = SpellChecker()

# Store the current typed word
typed_word = ""

def on_press(key):
    global typed_word

    try:
        if key.char:  # Key.char is the actual letter typed
            typed_word += key.char
    except AttributeError:
        # Ignore special keys
        pass

def on_release(key):
    global typed_word

    # If space is pressed, check and auto-correct the word
    if key == Key.space:
        corrected_word = spell.correction(typed_word)

        if corrected_word != typed_word:
            # Remove the wrong word by simulating backspaces
            for _ in range(len(typed_word)):
                pyautogui.press('backspace')

            # Type the corrected word and add a space
            pyautogui.typewrite(corrected_word)
            pyautogui.press('space')

        typed_word = ""  # Reset the current word buffer

# Set up the listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
