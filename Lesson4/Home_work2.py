data =[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def generator(data):
    count=0
    sizelist=len(data)
    while count<sizelist:
        if data[count]<data[count+1]:
            yield data[count+1]
        count+=1

gen=generator(data)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

