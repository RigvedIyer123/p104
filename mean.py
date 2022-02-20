import csv

with open('HW.csv') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newData = []
for i in range(len(filedata)):
    num = filedata[i][1]
    newData.append(float(num))

n = len(newData)
total = 0
for x in newData:
    total+=x

mean  = total/n
print("mean"+str(mean))