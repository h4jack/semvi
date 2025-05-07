from math import gcd

# Compute modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Encrypt using Affine Cipher
def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")

    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            encrypted = (a * x + b) % 26
            result += chr(encrypted + base)
        else:
            result += char
    return result


# Decrypt using Affine Cipher
def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"Modular inverse of {a} does not exist. Decryption impossible.")

    result = ""
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            decrypted = (a_inv * (y - b)) % 26
            result += chr(decrypted + base)
        else:
            result += char
    return result


# Main program
if __name__ == "__main__":
    mode = input("Enter mode ('encrypt' or 'decrypt'): ").lower()
    message = input("Enter message: ")
    a = int(input("Enter key 'a' (must be coprime to 26): "))
    b = int(input("Enter key 'b': "))

    if mode == "encrypt":
        result = affine_encrypt(message, a, b)
    elif mode == "decrypt":
        result = affine_decrypt(message, a, b)
    else:
        result = "Invalid mode!"

    print(f"\nResult: {result}")


# Example Input and Output
# PS S:\Cryptographics> py .\affine-cipher.py
# Enter mode ('encrypt' or 'decrypt'): encrypt       
# Enter message: Vulnerability
# Enter key 'a' (must be coprime to 26): 5
# Enter key 'b': 4

# Result: Fahrylejshsvu

# PS S:\Cryptographics> py .\affine-cipher.py
# Enter mode ('encrypt' or 'decrypt'): decrypt
# Enter message: Fahrylejshsvu
# Enter key 'a' (must be coprime to 26): 5
# Enter key 'b': 4

# Result: Vulnerability