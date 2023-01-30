# Saksham Singh
# 2022434
# Section B,  Group 7
# MTH Assignment 01

import math

file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/MTH100 A1/matrix.txt", "r+")
mtx = [list(map(float,i.split())) for i in file]

rows = len(mtx)
cols = len(mtx[0])

def swap(r1,r2):
        r1, r2 = r2, r1
        return r1, r2

def pivot_divide(lst):
    i = 0
    if lst[0]==0:
        if set(lst)=={0}:
            pass
        else:
            while lst[i]==0:
                if lst[i+1]==0:
                    pass
                else:
                    lst=list(map(lambda a: a/lst[i+1],lst))
                i+=1                
    else:
        lst=list(map(lambda a: a/lst[0],lst))
    return lst

def forward_el(matrix):
    global rows, cols
    # for i in range(rows-1):
    #     if matrix[i][i]==0:
    #         for j in range(i+1,rows):
    #             if matrix[j][i]==0:
    #                 if j<rows-1:
    #                     pass
    #                 elif j==rows-1:
    #                     print("Matrix is singular, the only solution is a trivial solution")
    #                     return None
    #             else:
    #                 matrix[i],matrix[j] = swap(matrix[i],matrix[j])

    #     for k in range(i+1,rows):
    #         r = matrix[k][i]/matrix[i][i]
    #         matrix[k] = [matrix[k][x]-r*matrix[i][x] for x in range(cols)]

    i = 0
    for j in range(cols):
        if i >= rows:
            break
        
        for k in range(i, rows):
            if matrix[k][j] != 0:
                matrix[i], matrix[k] = swap(matrix[i], matrix[k])
                break
        
        if matrix[i][j] == 0:
            continue
        
        pivot = matrix[i][j]
        for k in range(i+1, rows):
            scale = matrix[k][j] / pivot
            for l in range(j, cols):
                matrix[k][l] -= scale * matrix[i][l]
        i += 1

    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],3)

    for i in range(rows):
        matrix[i] = pivot_divide(matrix[i])
    
    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],3)

    return matrix

def back_sub(matrix):
    global rows, cols
    if cols>=rows:
        for i in range(1,rows):
            if matrix[i][i]==1:
                for j in range(i):
                    if matrix[j][i]==0:
                        pass
                    else:
                        matrix[j] = [matrix[j][k] - matrix[j][i]*matrix[i][k] for k in range(cols)]
            elif matrix[i][i]==0:
                for k in range(i,cols):
                    if matrix[i][k]==1:
                        for j in range(i):
                            if matrix[j][k]==0:
                                pass
                            else:
                                matrix[j] = [matrix[j][x] - matrix[j][k]*matrix[i][x] for x in range(cols)]
    else:
        for i in range(1,cols):
            if matrix[i][i]==1:
                for j in range(i):
                    if matrix[j][i]==0:
                        pass
                    else:
                        matrix[j] = [matrix[j][k] - matrix[j][i]*matrix[i][k] for k in range(cols)]
            elif matrix[i][i]==0:
                for k in range(i,cols):
                    if matrix[i][k]==1:
                        for j in range(i):
                            if matrix[j][k]==0:
                                pass
                            else:
                                matrix[j] = [matrix[j][x] - matrix[j][k]*matrix[i][x] for x in range(cols)]    

    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],3)
            if matrix[x][y] == -0:
                matrix[x][y] = int(matrix[x][y])
            elif math.modf(matrix[x][y])[0] == 0:
                matrix[x][y] = int(matrix[x][y])

    return matrix

def parm(matrix):
    global rows, cols, pivot_list, col_list, non_pivots
    pivot_list = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]!=0:
                pivot_list.append(j)
                break
    # print(pivot_list)
    col_list = [i for i in range(cols)]
    non_pivots = [i for i in col_list if i not in pivot_list]
    # print(non_pivots)

    
    # vectors = []
    # for i in col_list:
    #     col_i = []
    #     for j in range(rows):
    #         col_i.append(matrix[j][i])
    #     vectors.append(col_i)
    # # print(vectors)

    for i in non_pivots:
        # print(vectors[i])
        print('x{} is free'.format(i+1))
    print("----------------------------------------------")

    # for i in range(rows):
    #     lst = []
    #     for j in range(cols):
    #         if matrix[i][j]==1:
    #             lst.append[j]
    #             break
    #     for j in range(lst[0]+1,cols):
    #         if matrix[i][j]!=0:
    #             lst.append((-1*matrix[i][j],j))

    # for key in dic:
    #     print("x{} =".format(key+1), end="")
    #     for i in dic[key]:
    #         print(" {}*x{} +".format(i[0],i[1]+1), end="")

    trans_mtx = list(zip(*matrix))

    vectors = []
    for i in non_pivots:
        if len(trans_mtx[i]) == len(matrix[0]):
            temp = trans_mtx
        else:
            temp = [float(0)]*len(matrix[0])
        for j in range(len(temp)):
            if j == i: temp[j] = 1

        for j in range(len(trans_mtx)):
            if j == i:
                for k in range(len(trans_mtx[j])):
                    if trans_mtx[j][k] != float(0):
                        temp[pivot_list[k]] = -trans_mtx[j][k]
        vectors.append(temp)
    # x = parm(rref_mtx)
    for i in range(len(vectors)):
        print(f"x{non_pivots[i]+1}{vectors[i]}", end = " + ") if i != (len(vectors)-1) else print(f"x{non_pivots[i]+1}{vectors[i]}")

ef_mtx = forward_el(mtx)
rref_mtx = back_sub(ef_mtx)

print("----------------------------------------------\nThe RREF matrix is:\n----------------------------------------------")
for i in rref_mtx:
    print("|",end=" ")
    for j in i:
        print(j,end="\t")
    print("|")
print("----------------------------------------------")

parm(rref_mtx)

