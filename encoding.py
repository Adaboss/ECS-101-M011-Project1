import csv

byteMapFile = open('byteMap.csv')
byteMap = csv.reader(byteMapFile)

with open('original.txt', 'r') as originalFile:
    original = originalFile.read()
    original.strip()

encoded = open('encoded.txt', 'wb')

for letter in range(len(original)):

    for row in byteMap:

        if original[letter] == row[0]:
            encoded.write(row[2])

