data= [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_data=[]

for elem in data:
    if data.count(elem)==1:
        new_data.append(elem)

print(new_data)
