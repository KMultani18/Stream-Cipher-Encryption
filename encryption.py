

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import os

def chacha20_encrypt(plaintext, key, nonce):
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext

# Load the books (plaintexts)
with open('SherlockHomes.txt', 'rb') as f1, open('Dracula.txt', 'rb') as f2:
    sherlock = f1.read()
    dracula = f2.read()

# Generate a key and nonce (same for both encryptions)
key = os.urandom(32)  # ChaCha20 key is 32 bytes (256 bits)
nonce = os.urandom(16)  # ChaCha20 nonce is 16 bytes

# Encrypt both books using the same key and nonce
ciphertext_sherlock = chacha20_encrypt(sherlock, key, nonce)
ciphertext_dracula = chacha20_encrypt(dracula, key, nonce)

# Save the ciphertexts
if not os.path.exists('output'):
    os.makedirs('output')

with open('output/ciphertext_sherlock.bin', 'wb') as f1, open('output/ciphertext_dracula.bin', 'wb') as f2:
    f1.write(ciphertext_sherlock)
    f2.write(ciphertext_dracula)

print("Encryption completed and ciphertexts saved in the 'output' folder!")
