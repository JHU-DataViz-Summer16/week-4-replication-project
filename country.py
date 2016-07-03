# convert table from bizarre format to something sensible

import csv

country = ''
arr = []

with open('country_table.csv', 'r') as cable:
    reader = csv.reader(cable)
    for r in reader:
#        print(r)
        arr.append(r)





with open ('data_tjson.csv', 'w+') as data:
    writer = csv.writer(data)
    for m in range(2, 34):
    #    print('m is ', m)
        for a in (arr):
            if (a[0] != 'Country'):
    #            print(a[0], arr[0][m], a[1], round(float(a[m]), 1))
                writer.writerow([a[0], arr[0][m], a[1], round(float(a[m]), 1)])



cable.close()
#data.close()

        
