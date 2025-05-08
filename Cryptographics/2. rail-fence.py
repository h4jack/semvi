def encrypt_rail_fence(text, rails):
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


def decrypt_rail_fence(cipher, rails):
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    # Mark the zigzag path with placeholders
    row, direction = 0, False
    for i in range(len(cipher)):
        fence[row][i] = '*'
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1

    # Fill the marked positions with cipher text
    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == '*' and index < len(cipher):
                fence[r][c] = cipher[index]
                index += 1

    # Read the message in zigzag order
    result = ''
    row, direction = 0, False
    for i in range(len(cipher)):
        result += fence[row][i]
        if row == 0 or row == rails - 1:
            direction = not direction
        row += 1 if direction else -1

    return result


# Example usage
if __name__ == "__main__":
    message = input("Enter your message: ").replace(" ", "")
    rails = int(input("Enter number of rails: "))
    mode = input("Enter mode ('encrypt' or 'decrypt'): ").lower()

    if mode == 'encrypt':
        output = encrypt_rail_fence(message, rails)
    elif mode == 'decrypt':
        output = decrypt_rail_fence(message, rails)
    else:
        output = "Invalid mode!"

    print(f"\nResult: {output}")


# Example Input and Output
# PS C:\Cryptographics> py .\rail-fence.py
# Enter your message: hello crypt   
# Enter number of rails: 4
# Enter mode ('encrypt' or 'decrypt'): encrypt

# Result: hrecyloplt
# PS C:\Cryptographics> py .\rail-fence.py
# Enter your message: hrecyloplt
# Enter number of rails: 4
# Enter mode ('encrypt' or 'decrypt'): decrypt

# Result: hellocrypt