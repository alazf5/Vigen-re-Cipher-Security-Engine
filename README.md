# Interactive Vigenère & Autokey Cipher Engine

A lightweight, interactive Python application for encrypting and decrypting text using classical cryptographic methods. Built with modularity and clean execution in mind, this tool supports both standard **Vigenère Cipher** and **Autokey Cipher** variants, complete with flexible input sanitization options.

---

## Key Features

* **Dual Cipher Modes:**
  * **Standard Vigenère Cipher:** Encrypts text using key repetition logic across alphabetic characters.
  * **Autokey Vigenère Cipher:** Extends key generation using the plaintext (during encryption) or ciphertext (during decryption) to resist frequency analysis.
* **Strict Mode Option:** Optionally strips non-alphabetic characters (spaces, punctuation, numbers) before processing.
* **Case & Format Preservation:** Maintains upper/lowercase formatting in non-strict modes while ignoring non-alphabetic shifts smoothly.
* **Interactive CLI:** Guided command-line interaction with built-in input validation and recursive operation loops.

---

## How It Works

1. **Input Sanitization:** Filters characters based on configuration (`strict` vs standard mode).
2. **Dynamic Key Generation:** Generates key streams on-the-fly depending on the selected cipher mode.
3. **Shift Calculation:** Computes modulo 26 positional shifts per letter ($(P_i + K_i) \pmod{26}$ for encryption, $(C_i - K_i) \pmod{26}$ for decryption).

---

## Usage

Run the program via Python 3:

```bash
python main.py
