opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

column = extract (apps_data, 4)

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean (data_set, index, column):
    extract (data_set, index)
    find_sum (column)
    find_length (column)
    return find_sum(column) / find_length(column)
    
a = extract (apps_data, 4)
#print (a)

b = find_sum (a)
#print (b)

c = find_length (a)
#print (c)

avg_price = mean (apps_data, 4, a)
print (avg_price)