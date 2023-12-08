def inter_num_lst():
    sum_num = 0
    while True:
        num_list = input()
        for i in num_list.split():
            if i.isdigit():
                sum_num+=int(i)
            else:
                return sum_num
        print(f"Ədədlərin cəmi: {sum_num}")
    return sum_num


print(inter_num_lst())