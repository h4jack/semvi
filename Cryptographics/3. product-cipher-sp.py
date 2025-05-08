# Substitution: Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)


# Transposition: Rail Fence Cipher
def rail_fence_encrypt(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    row, direction = 0, False

    for i, char in enumerate(text):
        fence[row][i] = char
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1

    result = ''
    for r in range(rails):
        for c in range(len(text)):
            if fence[r][c] != '\n':
                result += fence[r][c]
    return result


def rail_fence_decrypt(cipher, rails):
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    row, direction = 0, False

    for i in range(len(cipher)):
        fence[row][i] = '*'
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1

    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == '*' and index < len(cipher):
                fence[r][c] = cipher[index]
                index += 1

    result = ''
    row, direction = 0, False
    for i in range(len(cipher)):
        result += fence[row][i]
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1

    return result


# Product Cipher Functions
def product_cipher_encrypt(text, shift, rails):
    text = text.replace(" ", "")
    substituted = caesar_encrypt(text, shift)
    encrypted = rail_fence_encrypt(substituted, rails)
    return encrypted


def product_cipher_decrypt(cipher, shift, rails):
    transposed = rail_fence_decrypt(cipher, rails)
    decrypted = caesar_decrypt(transposed, shift)
    return decrypted


# Main program
if __name__ == "__main__":
    mode = input("Enter mode ('encrypt' or 'decrypt'): ").lower()
    message = input("Enter message: ")
    shift = int(input("Enter Caesar cipher shift value: "))
    rails = int(input("Enter number of Rail Fence rails: "))

    if mode == "encrypt":
        result = product_cipher_encrypt(message, shift, rails)
    elif mode == "decrypt":
        result = product_cipher_decrypt(message, shift, rails)
    else:
        result = "Invalid mode!"

    print(f"\nResult: {result}")


# Example Input and Output
# S S:\Cryptographics> py .\product-cipher-sp.py
# Enter mode ('encrypt' or 'decrypt'): encrypt
# Enter message: hello world
# Enter Caesar cipher shift value: 3
# Enter number of Rail Fence rails: 4

# Result: krhzuoroog
# PS S:\Cryptographics> py .\product-cipher-sp.py
# Enter mode ('encrypt' or 'decrypt'): decrypt
# Enter message: krhzuoroog
# Enter Caesar cipher shift value: 3
# Enter number of Rail Fence rails: 4

# Result: helloworld