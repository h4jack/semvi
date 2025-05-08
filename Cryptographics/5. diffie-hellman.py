def mod_exp(base, exp, mod):
    res = 1
    base %= mod
    while exp:
        if exp % 2: 
            res = res * base % mod
        base = base * base % mod
        exp //= 2
    return res

def diffie_hellman(p, g, a, b):
    A, B = mod_exp(g, a, p), mod_exp(g, b, p)
    s1, s2 = mod_exp(B, a, p), mod_exp(A, b, p)
    return A, B, s1, s2

if __name__ == "__main__":
    p = int(input("Enter prime p: "))
    g = int(input("Enter primitive root g: "))
    a = int(input("Enter Alice's private key: "))
    b = int(input("Enter Bob's private key: "))
    A, B, s1, s2 = diffie_hellman(p, g, a, b)

    print("\n--- Key Exchange ---")
    print(f"Alice's Public Key: {A}")
    print(f"Bob's Public Key: {B}")
    print(f"Alice's Shared Secret: {s1}")
    print(f"Bob's Shared Secret: {s2}")

    if s1 == s2:
        print("✅ Shared secret key successfully established!")
    else:
        print("❌ Error: Shared secrets do not match.")



# Example Input and Output
# Enter a prime number (p): 103
# Enter a primitive root modulo p (g): 3
# Enter Alice's private key: 6
# Enter Bob's private key: 2

# --- Key Exchange ---
# Alice's Public Key: 8
# Bob's Public Key: 9
# Alice's Shared Secret: 64
# Bob's Shared Secret: 64
# ✅ Shared secret key successfully established!