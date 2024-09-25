

def xor_plaintexts(plaintext1, plaintext2, output_file):
    with open(plaintext1, 'rb') as f1, open(plaintext2, 'rb') as f2:
        sherlock = f1.read()
        dracula = f2.read()

    min_length = min(len(sherlock), len(dracula))

    xor_result = bytes([sherlock[i] ^ dracula[i] for i in range(min_length)])

    with open(output_file, 'wb') as output:
        output.write(xor_result)

# XOR the plaintexts and save the result
xor_plaintexts('SherlockHomes.txt', 'Dracula.txt', 'output/xor_plaintexts.bin')

print("XOR of plaintexts completed and saved as 'xor_plaintexts.bin' in the 'output' folder!")
