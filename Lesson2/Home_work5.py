my_list=[7,5,3,3,2]

new_elem=int(input())

i=0

while i<len(my_list):

    # print(len(my_list))
    if my_list[i]==new_elem:
         my_list.insert(i+1,new_elem)
         my_list.sort(reverse=True)
         break
    elif new_elem not in my_list:
        my_list.append(new_elem)
        my_list.sort(reverse=True)
        break
    i+=1



print(my_list)

