from csv import reader
from os import environ

output_dict = {}
with open('test.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        temp = row[0]
        region1 = temp.find(".")
        region2 = temp.find(".",region1+1)
        region_final = temp[region1+1:region2]
        
        environment2 = temp.find(".",region2+1)
        environment_final = temp[region2+1:environment2]
        # print(region_final+","+environment_final)
        key = region_final+","+environment_final
        if key not in output_dict.keys():
            output_dict[key] = 1
        else:
            output_dict[key] = output_dict[key]+1

for i in output_dict.keys():
    print(i+","+str(output_dict[i]))