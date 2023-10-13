import csv

with open('byteMapTest.csv') as byteMapFile:
    byteMapReader = csv.reader(byteMapFile)
    byteMap = list(byteMapReader)

with open('original.txt', 'r') as originalFile:
    original = originalFile.read()
    original.strip()
encoded = open('encoded.txt', 'w')

for letter in range(len(original)):
    for row in byteMap[1:]:
        if original[letter] == row[0]:
            encoded.write(row[2])
        break
encoded.close()
