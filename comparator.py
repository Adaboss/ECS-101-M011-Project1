import os

errors = 0
correctVal = 0

with open('encoded.txt', 'r') as encodedTxt:
    encoded = encodedTxt.read()
    encoded_file_size = len(encoded)/8

with open('decoded.txt', 'r') as decodedTxt:
    decoded = decodedTxt.read()
    decoded.strip()

with open('original.txt', 'r') as originalTxt:
    original = originalTxt.read()
    original.strip()
    original_file_size = os.path.getsize(original)

for i in range(len(original)):

    if original[i] != decoded[i]:
        errors += 1
    else:
        correctVal += 1

correctness = correctVal / len(original) * 100
compressionRate = encoded_file_size / original_file_size
print(f"Correctness: {correctness}")
print(f"Compression Rate: {compressionRate}")
