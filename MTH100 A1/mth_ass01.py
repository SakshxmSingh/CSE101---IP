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
    for i in range(rows-1):
        if matrix[i][i]==0:
            for j in range(i+1,rows):
                if matrix[j][i]==0:
                    if j<rows-1:
                        pass
                    elif j==rows-1:
                        print("Matrix is singular, the only solution is a trivial solution")
                        return None
                else:
                    matrix[i],matrix[j] = swap(matrix[i],matrix[j])

        for k in range(i+1,rows):
            r = matrix[k][i]/matrix[i][i]
            matrix[k] = [matrix[k][x]-r*matrix[i][x] for x in range(cols)]

    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],2)

    for i in range(rows):
        matrix[i] = pivot_divide(matrix[i])
    
    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],2)

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
            matrix[x][y]=round(matrix[x][y],2)
            if matrix[x][y] == -0:
                matrix[x][y] = int(matrix[x][y])
            elif math.modf(matrix[x][y])[0] == 0:
                matrix[x][y] = int(matrix[x][y])

    return matrix

ef_mtx = forward_el(mtx)
rref_mtx = back_sub(ef_mtx)

print("------------------------------------\nThe RREF matrix is:")
for i in rref_mtx:
    print("|",end=" ")
    for j in i:
        print(j,end="\t")
    print("|")

