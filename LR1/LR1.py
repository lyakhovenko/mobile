import csv

list_1 = []

with open('data.csv') as data_file:
    reader = csv.reader(data_file)
    for a in reader:
        list_1.append(a)

number = '915783624'
k = 1
s = 5
minut_call = 0.0
coat_sms = 0

for i in range(9):
    if number in list_1[i][1]:
        if float(list_1[i][3]) > 10:
            minut_call += float(list_1[i][3])-10.0
            coat_sms += float(list_1[i][4])
        else:
            coat_sms += float(list_1[i][4])
        
minut_call = round(minut_call, 2)

out = open('output.txt', 'w')
print(str(coat_sms*s), str(k*minut_call), file = out)

data_file.close
out.close