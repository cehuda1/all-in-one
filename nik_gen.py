import csv
import random
import datetime
from termcolor import colored

data = []

limit = 5
current_date = datetime.datetime.now().date()
try:
    with open('counter.txt', 'r') as f:
        date, counter = f.read().strip().split(',')
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        counter = int(counter)
        if date == current_date:
            if counter >= limit:
                print(f"\nBatas sudah tercapai hari ini, silahkan coba lagi besok")
                exit()

        else:
            counter = 0
except FileNotFoundError:
    counter = 0
    date = current_date

with open('env.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    next(reader)
    row = random.choice(list(reader))
    nomor = row[1].strip()
    nomor_kk = row[2].strip()
    nik = row[3].strip()
    data.append([nomor, nomor_kk, nik])

print("\n+--------------------+------------------+")
print("|      Nomor KK      |       NIK        |")
print("+--------------------+------------------+")
for d in data:
    print("|  {1}  | {2} |".format(d[0], d[1], d[2]))
    print("+--------------------+------------------+\n")
    print(f"Data telah di generate sebanyak " + (colored((counter+1),'green') + " kali"))
    print(f"tersisa " + (colored(( limit - 1 - counter ),'red') + " kesempatan"))

counter += 1
with open('counter.txt', 'w') as f:
    f.write(f"{current_date},{counter}")
