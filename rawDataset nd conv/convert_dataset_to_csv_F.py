filecnt = 100
folderName = "D:\\iit_thesis\\dataset_eeg\\F\\F"

data = ["" for i in range(filecnt)]
  
# Reading data from file1 

for i in range(1,filecnt+1):
    name = folderName + str(i).zfill(3) + ".txt"
    with open(name) as fp:
        data[i-1] = list(fp.read().split('\n'))

fin = zip(*data)
# print(data)
t = [list(a) for a in fin]
# print(t)
import csv
with open('D.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for data in t:
        writer.writerow(data)
