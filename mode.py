from collections import Counter

import csv

with open('HW.csv') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newData = []
for i in range(len(filedata)):
    num = filedata[i][1]
    newData.append(float(num))

data = Counter(newData)
mode = {
    "50-60":0,"60-70":0,"70-80":0
}
for h ,occurence in data.items():
    if(50<float(h)<60):
        mode["50-60"]+=occurence
    elif(60<float(h)<70):
        mode["60-70"]+=occurence
    elif(70<float(h)<80):
        mode["70-80"]+=occurence
moder,modeo = 0,0
for range,occurence in mode.items():
    if(occurence>modeo):
        moder,modeo = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((moder[0]+moder[1])/2)
print(f"mode is=>{mode:2f}")