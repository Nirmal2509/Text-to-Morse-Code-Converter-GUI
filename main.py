import tkinter as tk
from tkinter import messagebox
import pygame
import time

# Initialize pygame for sound
pygame.mixer.init()

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse dictionary for Morse-to-Text
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def text_to_morse():
    """Converts text to Morse Code and displays it in the output box."""
    text = text_entry.get().upper()
    morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    output_text.set(morse_code)


def morse_to_text():
    """Converts Morse Code to text and displays it in the output box."""
    morse = text_entry.get().strip().split()
    text = ''.join(REVERSE_MORSE_CODE_DICT.get(code, '') for code in morse)
    output_text.set(text)


def play_morse():
    """Plays the Morse Code as beeps."""
    morse_code = output_text.get()

    if not morse_code:
        messagebox.showwarning("Warning", "No Morse Code to play!")
        return

    for symbol in morse_code:
        if symbol == '.':
            pygame.mixer.Sound("dot.wav").play()
            time.sleep(0.2)
        elif symbol == '-':
            pygame.mixer.Sound("dash.wav").play()
            time.sleep(0.4)
        elif symbol == '/':
            time.sleep(0.6)
        time.sleep(0.2)


def copy_to_clipboard():
    """Copies the output text to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(output_text.get())
    root.update()
    messagebox.showinfo("Copied", "Morse Code copied to clipboard!")


# Create the GUI window
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("400x400")
root.resizable(False, False)

# Input Label & Entry
tk.Label(root, text="Enter Text / Morse Code:", font=("Arial", 12)).pack(pady=5)
text_entry = tk.Entry(root, width=40, font=("Arial", 12))
text_entry.pack(pady=5)

# Output Label
tk.Label(root, text="Output:", font=("Arial", 12)).pack(pady=5)
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, font=("Arial", 14, "bold"),
                        fg="black", bg="lightgray", wraplength=380, padx=10, pady=5)
output_label.pack(pady=5)

# Buttons
tk.Button(root, text="Convert to Morse", command=text_to_morse, font=("Arial", 12), width=20).pack(pady=5)
tk.Button(root, text="Convert to Text", command=morse_to_text, font=("Arial", 12), width=20).pack(pady=5)
tk.Button(root, text="Play Morse Code", command=play_morse, font=("Arial", 12), width=20).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), width=20).pack(pady=5)

# Run the GUI loop
root.mainloop()

