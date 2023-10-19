import csv
import os

with open('byteMapTest.csv') as byteMapFile:
    byteMapReader = csv.reader(byteMapFile)
    byteMap = list(byteMapReader)

with open('example1.txt', 'r') as originalFile:
    original = originalFile.read()
temp = open('temp.txt', 'w')

for letter in range(len(original)):
    for row in byteMap[1:]:
        if original[letter] == row[0]:
            temp.write(row[2])

encoded = open('encoded.txt', 'w')
temp = open('temp.txt', 'r')
temp_string = temp.read()
temp_len = str(len(temp_string))
print((os.path.getsize('temp.txt'))/8)
encoded.write(temp_len + '.' + temp_string)
encoded.close()
