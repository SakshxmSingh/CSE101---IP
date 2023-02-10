l=[1,1,2,2,1,3,2,4,5,2,6,7,8,9]
l_set = set(l)

dic = {}
for key in l_set:
    indexes = []
    for i in range(len(l)):
        if l[i]==key:
            indexes.append(i)
    dic.update({key:indexes})

n = int(input("Enter integer to check: "))

if n in dic:
    print(f"frequency is {len(dic[n])} and indexes are {dic[n]}")
else:
    print("Number not in list")
