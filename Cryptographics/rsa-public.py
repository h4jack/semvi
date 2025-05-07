import random
from math import gcd

# Generate a small prime number (for demo only; use large primes for real use)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(min_val=100, max_val=300):
    while True:
        p = random.randint(min_val, max_val)
        if is_prime(p):
            return p

# Extended Euclidean Algorithm to find modular inverse
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    g, x, _ = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi

# RSA Key Generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# Encryption
def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Decryption
def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Main
if __name__ == "__main__":
    print("🔐 RSA Key Generation")
    public_key, private_key = generate_keys()
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    message = input("\nEnter a message to encrypt: ")
    encrypted = encrypt(message, public_key)
    print(f"\n🔒 Encrypted: {encrypted}")

    decrypted = decrypt(encrypted, private_key)
    print(f"🔓 Decrypted: {decrypted}")


# Example Input and Output
# 🔐 RSA Key Generation
# Public Key (e, n): (51747, 64291)
# Private Key (d, n): (61675, 64291)

# Enter a message to encrypt: RSAIsGodPlayer

# 🔒 Encrypted: [20631, 10307, 41105, 41311, 25727, 16114, 30620, 58818, 53113, 27601, 26838, 50324, 12260, 16650]
# 🔓 Decrypted: RSAIsGodPlayer