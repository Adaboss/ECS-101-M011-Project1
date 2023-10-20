import csv
import os
with open('byteMap.csv') as byteMapFile:
    byteMapReader = csv.reader(byteMapFile)
    byteMap = list(byteMapReader)

file = input("Please enter original file name: ")
originalTxt = open(file)
original = originalTxt.read()

temp = open('temp.txt', 'w')

for letter in range(len(original)):
    count = 0
    for row in byteMap:
        if original[letter] == row[0]:
            temp.write(row[2])
            count = 0
        count +=1
        if count == 62:
            temp.write(row[2])

temp.close()
encoded = open('encoded.txt', 'w')
temp = open('temp.txt', 'r')
temp_string = temp.read()
temp_len = str(len(temp_string))
print((os.path.getsize('temp.txt'))/8)
encoded.write(temp_len + '.' + temp_string)
encoded.close()
