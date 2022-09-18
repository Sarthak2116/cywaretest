from csv import reader
from os import environ

region_input = input('region=')
environment_input = input('environment=')
input_row = ""
list_of_rows = []
with open('test.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        temp = row[0]
        region1 = temp.find(".")
        region2 = temp.find(".",region1+1)
        region_final = temp[region1+1:region2]
        
        environment2 = temp.find(".",region2+1)
        environment_final = temp[region2+1:environment2]
        if region_final == region_input and environment_final == environment_input:
            input_row = temp
            list_of_rows.append(temp)


for i in range(10,51):
    seq_end = input_row.find("-")
    seq_start = seq_end-2
    seq_final = input_row[seq_start:seq_end]
    prefix = input_row[0:seq_start]
    postfix = input_row[seq_end:]
    # print(postfix)
    check_row = prefix+str(i)+postfix
    if check_row not in list_of_rows:
        print(check_row)