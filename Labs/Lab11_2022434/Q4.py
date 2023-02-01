import numpy

n = int(input())
p = int(input())
k = int(input())
m = int(input())

mat1 = []
for i in range(n):
    temp = [int(i) for i in list(input().split())]
    mat1.append(temp)
    
mat2 = []
for i in range(k):
    temp = [int(i) for i in list(input().split())]
    mat2.append(temp)
    
np_mat1 = numpy.array(mat1)
np_mat2 = numpy.array(mat2)

try:
    mult = numpy.dot(np_mat1, np_mat2)
    for i in range(len(mult)):
        for j in range(len(mult[0])):
            print(float(mult[i][j]), end=' ')
        print()
except:
    print("Dimensions of matrices are not compatible")