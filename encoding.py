with open('byteMap.csv', 'r') as byteMapFile:
    byteMap = byteMapFile.read()
with open('original.txt', 'r') as originalFile:
    original = originalFile.read()
    original.strip()
with open('encoded.txt', 'w+b') as encodedFile:
    encoded = encodedFile.read()
    encoded.strip()
