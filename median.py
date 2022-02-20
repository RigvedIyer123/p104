import csv
import statistics

with open('HW.csv') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newData = []
for i in range(len(filedata)):
    num = filedata[i][1]
    newData.append(float(num))

n = len(newData)
newData.sort()
if(n%2==0):
    m1 = float(newData[n//2])
    m2 = float(newData[n//2-1])
    median = (m1+m2)/2
else:
    median = newData[n//2]
    print(n)

print ("median = "+str(median))