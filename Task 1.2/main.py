import random
from itertools import combinations

lst = []
new_lst = []
copy_lst1 = []
num = int(input('Enter the number of elements in list: '))

for i in range(num):
    lst.append(input())

for binary in lst:
    res = int(binary, 2)
    new_lst.append(res)

print(f"lst = {lst}")
print(f"new_lst = {new_lst}\n")

copy_lst1.extend(new_lst)

print("Calculating for random difference:")

for i in range(0,len(lst)-2):
    n1 = random.choice(new_lst)
    new_lst.remove(n1)
    n2 = random.choice(new_lst)
    new_lst.remove(n2)
    sum = n1 + n2
    new_lst.append(sum)
    print(f"new_lst = {new_lst}\n")

diff = abs(new_lst[0] - new_lst[1])
print(diff)

print("\n\nCalculating for least difference:")

diff_list=[]

def MinimumDiff(lst):
    combination = combinations(lst, 2)
    for combo in combination:
        copy_lst2 = []
        copy_lst2.extend(lst)
        n1 = combo[0]
        copy_lst2.remove(n1)
        n2 = combo[1]
        copy_lst2.remove(n2)
        sum = n1 + n2
        copy_lst2.append(sum)
        if len(copy_lst2) == 2:
            difference = abs(copy_lst2[0] - copy_lst2[1])
            diff_list.append(difference)
            print(copy_lst2)
        else:
            MinimumDiff(copy_lst2)



    return min(diff_list)

print(f"\nMinimum difference = {MinimumDiff(copy_lst1)}")

'''0001
0011
0101
1011
1101
1111'''