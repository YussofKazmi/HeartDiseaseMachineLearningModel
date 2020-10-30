import csv

lines = []

with open('processed.hungarian.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for line in csv_reader:
        values = [float(0) if x == '?' else float(x) for x in line]
        lines.append(values)
        
with open('input.txt', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for i in lines:
        csv_writer.writerow(i)

        