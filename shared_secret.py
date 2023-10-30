import random

# Public parameters agreed upon by both parties
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Generate private keys for both parties
a = random.randint(1, p - 1)  # Party A's private key
b = random.randint(1, p - 1)  # Party B's private key

# Compute public values to be exchanged
A = (g ** a) % p
B = (g ** b) % p

# Shared secret calculation
shared_secret_A = (B ** a) % p
shared_secret_B = (A ** b) % p

# Both parties should have the same shared secret
assert shared_secret_A == shared_secret_B

print("Shared Secret:", shared_secret_A)