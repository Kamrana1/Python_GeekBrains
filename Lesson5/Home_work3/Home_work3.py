lst=[]
parts=[]

with open("data.txt", 'r') as f:
    for line in f:
        parts=line.split(" ")
        if int(parts[1])<20000:
            print(f"{parts[0]} {parts[1]}", end=" ")


