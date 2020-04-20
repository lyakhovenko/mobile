import csv
import matplotlib.pyplot as plt

list_1 = []

with open('dataset.csv') as data_file:
    reader = csv.reader(data_file)
    for a in reader:
        list_1.append(a)

k = 0.5
limit = 1000
address = '192.168.250.39'
Q = 0.0
x = []
y = []

for i in range(17449):
    if address in list_1[i][3]:
        Q += float(list_1[i][12])
        x.append(float(list_1[i][2]))
        y.append(float(list_1[i][12]))

Q -= 1000
X = Q*k

out = open('output.txt', 'w')
print(X, file = out)

data_file.close
out.close

x.sort()
y.sort()
assert len(x) == len (y)
plt.plot(x, y)
plt.grid(True)
plt.show()







