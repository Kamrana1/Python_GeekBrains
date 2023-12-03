seconds=input("Saniyələri daxil edin: ")

hours = int(int(seconds)/3600)
print(max(5, 6, key=None))
minuts = int(max(int(seconds)-hours*3600, 0, key=None)/60)
seconds = max(int(seconds) - hours*3600 - minuts*60, 0, key=None)
print(hours, ":", minuts, ":", seconds)
