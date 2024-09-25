

def xor_files(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        ciphertext_sherlock = f1.read()
        ciphertext_dracula = f2.read()

    # Ensure both files are the same length
    min_length = min(len(ciphertext_sherlock), len(ciphertext_dracula))

    xor_result = bytes([ciphertext_sherlock[i] ^ ciphertext_dracula[i] for i in range(min_length)])

    with open(output_file, 'wb') as output:
        output.write(xor_result)

# XOR the two ciphertexts and save the result
xor_files('output/ciphertext_sherlock.bin', 'output/ciphertext_dracula.bin', 'output/xor_ciphertexts.bin')

print("XOR of ciphertexts completed and saved as 'xor_ciphertexts.bin' in the 'output' folder!")
