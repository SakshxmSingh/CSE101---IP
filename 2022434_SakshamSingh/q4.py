import itertools

l1 = [1,2,3,4]
l2 = [9,8,7,6]

lst = l1+l2

# def tuplecreator(lst1,lst2,i=0):
#     lst = []
#     if i==len(lst1):
#         pass
#     else:
#         lst.append((lst1[i],lst2[i]))
#         return ls

lst = list(itertools.combinations(lst,2))
print((lst))
