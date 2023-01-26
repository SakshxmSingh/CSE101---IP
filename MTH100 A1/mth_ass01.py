# Saksham Singh
# 2022434
# Section B,  Group 7
# MTH Assignment 01

file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/MTH100 A1/matrix.txt", "r+")
mtx = [list(map(float,i.split())) for i in file]
print(mtx)

rows = len(mtx)
cols = len(mtx[0])

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
    def swap(r1,r2):
        r1, r2 = r2, r1
        return r1, r2
    
    for i in range(rows-1):
        if matrix[i][i]==0:
            for j in range(i+1,rows):
                if matrix[j][i]==0:
                    if j<rows-1:
                        pass
                    elif j==rows-1:
                        return str("Matrix is singular, the only solution is a trivial solution")
                else:
                    matrix[i],matrix[j] = swap(matrix[i],matrix[j])

        for k in range(i+1,rows):
            r = matrix[k][i]/matrix[i][i]
            matrix[k] = [matrix[k][x]-r*matrix[i][x] for x in range(cols)]

    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],3)

    for i in range(rows):
        matrix[i] = pivot_divide(matrix[i])
    
    for x in range(rows):
        for y in range(cols):
            matrix[x][y]=round(matrix[x][y],3)

    return matrix

ef_mtx = forward_el(mtx)

print(ef_mtx)



