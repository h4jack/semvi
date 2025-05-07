def caesar_cipher(text, shift, mode='e'):
    result = ""
    
    if mode == 'd':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces, punctuation, etc. unchanged
    
    return result


# Example usage
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    mode = input("Enter Encryption or Decryption mode as ('e' or 'd'): ").lower()

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult: {output}")


# Example Input and Output

# PS S:\Cryptographics> py .\ceasar-cipher.py
# Enter your message: Information Security
# Enter shift value (e.g., 3): 12
# Enter Encryption or Decryption mode as ('e' or 'd'): e

# Result: Uzradymfuaz Eqogdufk

# PS S:\Cryptographics> py .\ceasar-cipher.py
# Enter your message: Uzradymfuaz Eqogdufk
# Enter shift value (e.g., 3): 12
# Enter Encryption or Decryption mode as ('e' or 'd'): d

# Result: Information Security