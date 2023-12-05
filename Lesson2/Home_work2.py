lst=[]
i=0
while i<10:
    i+=1
    element=input("Elementi daxil edin: ")
    lst.append(element)

i=0
while i<9:
    element=lst[i]
    lst[i]=lst[i+1]
    lst[i+1]=element
    i += 2

print(lst)