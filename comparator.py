import os

errors = 0
correctVal = 0

with open('temp.txt', 'r') as encodedTxt:
    encoded = encodedTxt.read()
    encoded_file_size = len(encoded) / 8

with open('decoded.txt', 'r') as decodedTxt:
    decoded = decodedTxt.read()
    decoded.strip()

file = input("Please enter original file name: ")
originalTxt = open(file, encoding='utf-8', errors='replace')
original = originalTxt.read()
original_file_size = os.path.getsize(file)
for i in range(len(original)):

    if original[i] != decoded[i]:
        print(original[i], decoded[i])
        errors += 1
    else:
        correctVal += 1

correctness = correctVal / len(original) * 100
compressionRate = 1- (encoded_file_size /  original_file_size)
print(f"Correctness: {correctness}")
print(f"Compression Rate: {compressionRate*100}")
