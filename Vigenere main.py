import sys


def get_shift(char):
    """Helper to get 0-25 index for a character (A=0, B=1...)."""
    if char.islower():
        return ord(char) - 97
    else:
        return ord(char) - 65


def shift_char(char, shift_amount, mode='encrypt'):
    """
    Shifts a single character by shift_amount.
    mode: 'encrypt' adds the shift, 'decrypt' subtracts it.
    """
    base = 97 if char.islower() else 65
    original_pos = ord(char) - base

    if mode == 'encrypt':
        new_pos = (original_pos + shift_amount) % 26
    else:
        new_pos = (original_pos - shift_amount + 26) % 26

    return chr(new_pos + base)


def vigenere_engine(text, keyword, mode='encrypt', strict=False, autokey=False):
    """
    Unified engine for both encryption and decryption.
    """
    result = []

    # 1. Input Sanitization for Strict Mode
    if strict:
        text = ''.join(filter(lambda c: c.isalpha(), text))

    # 2. Key Preparation
    # We only care about alphabetic characters in the key
    key_stream = [c for c in keyword if c.isalpha()]

    if not key_stream:
        return "Error: Key must contain at least one letter."

    key_index = 0

    for char in text:
        if char.isalpha():
            # --- Key Selection Logic ---
            if autokey:
                # In Autokey, we read linearly from the growing key_stream
                if key_index < len(key_stream):
                    k_char = key_stream[key_index]
                else:
                    # Fallback (should not happen in valid logic flow)
                    k_char = 'A'
            else:
                # In Standard, we wrap around the keyword
                k_char = key_stream[key_index % len(key_stream)]

            # --- Shift Calculation ---
            shift = get_shift(k_char)
            processed_char = shift_char(char, shift, mode)
            result.append(processed_char)

            # --- Autokey Extension Logic ---
            if autokey:
                if mode == 'encrypt':
                    # Encrypt: Plaintext (char) extends the key
                    key_stream.append(char)
                else:
                    # Decrypt: Decrypted text (processed_char) extends the key
                    key_stream.append(processed_char)

            key_index += 1
        else:
            # Handle non-alpha chars
            if not strict:
                result.append(char)

    return "".join(result)


def get_bool_input(prompt):
    """Helper to handle Yes/No user inputs."""
    while True:
        choice = input(f"{prompt} (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print("Invalid input. Please enter 'y' or 'n'.")


def main():
    print("========================================")
    print("   Vigenère Cipher Tool (Interactive)")
    print("========================================")

    while True:
        print("\n--- New Operation ---")
        action = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").lower().strip()

        if action == 'q':
            print("Exiting tool. Goodbye!")
            sys.exit()

        if action not in ['e', 'd']:
            print("Invalid choice. Please select E, D, or Q.")
            continue

        operation_mode = 'encrypt' if action == 'e' else 'decrypt'

        # User Inputs
        text = input(f"Enter the text to {operation_mode}: ")
        keyword = input("Enter the keyword: ")

        # Configuration
        print("\n--- Configuration ---")
        use_strict = get_bool_input("Strict Mode? (Remove spaces/symbols)")
        use_autokey = get_bool_input("Autokey Mode? (Use text to extend key)")

        # Execution
        result = vigenere_engine(text, keyword, operation_mode, use_strict, use_autokey)

        print("\n" + "=" * 40)
        print(f"OUTPUT ({operation_mode.upper()}):")
        print(result)
        print("=" * 40)


if __name__ == "__main__":
    main()