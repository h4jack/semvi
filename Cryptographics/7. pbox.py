def pbox_encrypt(message, pbox):
    size = len(pbox)
    # Pad message to be a multiple of block size
    pad_len = (size - len(message) % size) % size
    message += ' ' * pad_len

    encrypted = ''
    for i in range(0, len(message), size):
        block = message[i:i + size]
        encrypted += ''.join(block[pbox[j]] for j in range(size))
    return encrypted

def pbox_decrypt(ciphertext, pbox):
    size = len(pbox)
    inverse = [0] * size
    for i, pos in enumerate(pbox):
        inverse[pos] = i

    decrypted = ''
    for i in range(0, len(ciphertext), size):
        block = ciphertext[i:i + size]
        decrypted += ''.join(block[inverse[j]] for j in range(size))
    return decrypted

# --- Main Program ---
message = input("Enter the message: ")
pbox = list(map(int, input("Enter P-box (0-based, space-separated): ").split()))

encrypted = pbox_encrypt(message, pbox)
decrypted = pbox_decrypt(encrypted, pbox)

print(f"\nEncrypted: '{encrypted}'")
print(f"Decrypted: '{decrypted}'")




# Example Input and Output
# Enter the message: Information Security
# Enter P-box as space-separated indices (0-based): 4 2 3 1 0      

# Encrypted message: 'ronfIoiatmce Snytriu'
# Decrypted message: 'Information Security'
