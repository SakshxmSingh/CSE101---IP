# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------ques05------------------
input_list= [tuple(map(int,input("Enter coordinates:\n").split()))]
while input_list[-1]!=():
    input_list.append(tuple(map(int,input().split())))
input_list.pop()

# for i in input_list:
#     i = i + (1,)
# print(input_list)

mat = []
for i in range(len(input_list)):
    tup1 = (1,)
    mat.append(input_list[i])
    mat[i] = mat[i] + tup1

def matrix_scale(matric, cx, cy):
    scaling_matrix = [[cx,0,0],[0,cy,0],[0,0,1]]
    scaled_matrix = []
    final_coords = []
    for i in range(len(matric)):
        scaled_matrix.append((matric[i][0]*scaling_matrix[0][0],matric[i][1]*scaling_matrix[1][1],matric[i][2]*scaling_matrix[2][2]))
    for i in scaled_matrix:
        final_coords.append((i[0],i[1]))
    print(final_coords)

matrix_scale(mat,int(input('Enter cx: ')),int(input('Enter cy: ')))
     