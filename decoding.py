import csv

with open('temp.txt', 'r') as encodedFile:
    encoded = encodedFile.read()
    encoded.strip()
with open('byteMap.csv') as byteMapFile:
    byteMapReader = csv.reader(byteMapFile)
    byteMap = list(byteMapReader)
decoded = open('decoded.txt', 'w')

index = 0
lengthEncoded = len(encoded)

while index <= lengthEncoded-1:
    if encoded[index] == '1':
        for row in byteMap:
            if encoded[index:index + 4] == row[2]:
                print(row[0], encoded[index:index+4])
                decoded.write(row[0])
        index += 4
    else:
        for row in byteMap:
            if encoded[index:index + 8] == row[2]:
                print(row[0], encoded[index:index + 8])
                decoded.write(row[0])
        index += 8
