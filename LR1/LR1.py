import csv

list_1 = []

with open('data.csv') as data_file:
    reader = csv.reader(data_file)
    for a in reader:
        list_1.append(a)

number = '915783624'
k = 2
s = 1
minut_call = 0
coat_sms = 0

for i in range(9):
    if number in list_1[i][1]:
        minut_call += float(list_1[i][3])
        coat_sms += float(list_1[i][4])

out = open('output.txt', 'w')
if coat_sms <= 10:
    print('0', str(k*minut_call), file = out)
else: 
    print(str((coat_sms-10)*s), str(k*minut_call), file = out)

data_file.close
out.close