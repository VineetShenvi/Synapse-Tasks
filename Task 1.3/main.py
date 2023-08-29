encoded_lists = [
    [1, 2, 3, 4, 5, 6, 7,8,9, 112,113,114],
    [5, 7, 8, 9, 15],
    [12, 14, 16, 17, 18],
    [11, 12, 13, 16, 17, 18, 19, 20, 21]
]


user_list = []
temp_list = []

n = int(input('Enter the number of sub-lists: '))
for i in range(n):
    num = int(input('Enter the number of elements in sub - list: '))
    for j in range(num):
        temp_list.append(int(input()))
    user_list.append(temp_list)
    temp_list = []

print(f"Entered list: {user_list}")

def explode_chains(encoded_lists):
    decoded_list = []
    for row in encoded_lists:
        deleted_numbers = []
        count = 1
        updated_last = False
        last_index = 1
        for i in range(0,len(row)-1):
            if count == 3:
                deleted_numbers.extend(row[i + 1 - count : i + 1])
                count = 1
                updated_last = True
            if row[i]+1==row[i+1]:
                if not updated_last:
                    count+=1
                else:
                    updated_last = False
            else:
                count = 1
                updated_last = False
            last_index = i
        if count == 3:
            deleted_numbers.extend(row[last_index + 2 - count:last_index+ 2])
        for i in deleted_numbers:
            try:
                row.remove(i)
            except ValueError:
                pass
        decoded_list.append(row)

    print(f"Decoded list: {decoded_list}")

explode_chains(user_list)


