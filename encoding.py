import csv

byteMapFile = open('byteMapTest.csv')
byteMap = csv.reader(byteMapFile)

with open('original.txt', 'r') as originalFile:
    original = originalFile.read()
    original.strip()

encoded = open('encoded.txt', 'w')

for letter in range(len(original)):

    for row in byteMap:

        if original[letter] == row[0]:
            encoded.write(row[2])


encoded.close()