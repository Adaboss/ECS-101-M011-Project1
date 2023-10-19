import csv

with open('temp.txt', 'r') as encodedFile:
    encoded = encodedFile.read()
    encoded.strip()
with open('byteMapTest.csv') as byteMapFile:
    byteMapReader = csv.reader(byteMapFile)
    byteMap = list(byteMapReader)

index = 0
while index != range(len(encoded)):
    print(index)
    if encoded[index] == '1':
        for row in byteMap:

        print(encoded[index:index + 4])
        index += 4
    else:
        print(encoded[index:index + 8])
        index += 8
