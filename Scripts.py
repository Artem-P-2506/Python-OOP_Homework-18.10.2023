import os

def writeCharacteristicsToFile(sneakersOBJ, fileName):
    fileName += ".txt"
    with open(fileName, 'w') as file:
        file.write(sneakersOBJ.showCharacteristics())

def readCharacteristicsFromFile(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            temp = file.read().split("\n")
            result = []
            for line in temp:
                result.extend(line.split("\t"))
            result = result[1::2] # Использую "срез" для сохраненя только четных елементов масива
            if len(result) >= 7:
                result.pop()
        return result
    else:
        print("Invalid path!")