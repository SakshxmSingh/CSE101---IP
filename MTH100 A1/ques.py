# Saksham Singh
# 2022434
# Section B,  Group 7
# MTH Assignment 01

file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/MTH100 A1/matrix.txt", "r+")
mtx = [list(map(float,i.split())) for i in file]
print(mtx)

# def pivot_divide(lst):
#     i = 0
#     if lst[0]==0:
#         if set(lst)=={0}:
#             pass
#         else:
#             while lst[i]==0:
#                 if lst[i+1]==0:
#                     pass
#                 else:
#                     lst=list(map(lambda a: a/lst[i+1],lst))
#                 i+=1                
#     else:
#         lst=list(map(lambda a: a/lst[0],lst))
#     return lst

# print(pivot_divide(mtx[0]))

# def subtract_down(lst):
#     pass

# for i in len(range(mtx)):
#     for j in len(range(mtx[i])):
#         if mtx[i][j]


# def rref(matrix):
#     def swap(r1,r2):
#         r1, r2 = r2, r1
#         return r1, r2

#     lead = 0
#     ro = len(matrix)
#     col = len(matrix[0])
    
#     for r in range(ro):
#         if col<=lead:
#             break
#         i=r
#         while matrix[i][lead] == 0:
#             i+=1
#             if ro == i:
#                 i=r
#                 lead+=1
#                 if col == lead:
#                     break
#         if i!=r:
#             matrix[i],matrix[r]=swap(matrix[i],matrix[r])
#         for k in range(len(matrix[r])):
#             matrix[r][k]=matrix[r][k]/matrix[r][lead]
#         for j in range(ro):
#             if j!=r:
#                 for k in range(len(matrix[j])):
#                     matrix[j][k] = matrix[r][k]*matrix[j][lead]
#         lead+=1
#     return matrix
# print(rref(mtx))


