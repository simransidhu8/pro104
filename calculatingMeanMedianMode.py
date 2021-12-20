import csv 
from collections import Counter

with open("HeightWeight.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

newData = []

for i in range(len(file_data)):
    number = file_data[i][1]
    newData.append(float(number))

def mean():
    n = len(newData)
    total = 0

    for x in newData:
        total = total + x

    mean = total/n
    print("The mean is " + str(mean))

def median():
    newData.sort()

    n = len(newData)

    if n%2 == 0:
        median1 = float(newData[n//2])
        median2 = float(newData[n//2 -1])

        median = (median1 + median2) / 2
    else:
        median = newData[n//2]
    
    print("The median is" + str(median))

def mode():
    data = Counter(newData)

    mode_data_range = {
        "75 - 85": 0,
        "85 - 95": 0,
        "95 - 105": 0,
        "105 - 115": 0,
        "115 - 125": 0,
        "125 - 135": 0,
        "135 - 145": 0,
        "145 - 155": 0,
        "155 - 165": 0,
        "165 - 175": 0,
    }

    for height,occurence in data.items():
        if 75 < float(height) < 85:
            mode_data_range["75 - 85"] += occurence
        elif 85 < float(height) < 95:
            mode_data_range["85 - 95"] += occurence
        elif 95 < float(height) < 105:
            mode_data_range["95 - 105"] += occurence
        elif 105 < float(height) < 115:
            mode_data_range["105 - 115"] += occurence
        elif 115 < float(height) < 125:
            mode_data_range["115 - 125"] += occurence
        elif 125 < float(height) < 135:
            mode_data_range["125 - 135"] += occurence
        elif 135 < float(height) < 145:
            mode_data_range["135 - 145"] += occurence
        elif 145 < float(height) < 155:
            mode_data_range["145 - 155"] += occurence
        elif 155 < float(height) < 165:
            mode_data_range["155 - 165"] += occurence
        elif 165 < float(height) < 175:
            mode_data_range["165 - 175"] += occurence
    
    mode_range = 0
    mode_occurence = 0

    for range, occurence in mode_data_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1])/2)
    print(f"mode is {mode: 2f}")

def main():
    mean()
    median()
    mode()

main()
