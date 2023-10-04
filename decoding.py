
with open('byteMap.csv', 'r') as byteMapFile:
    byteMap = byteMapFile.read()

with open('encoded.txt', 'r') as encodedFile:
    encoded = encodedFile.read()
    encoded.strip()
