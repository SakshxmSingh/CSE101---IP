# to check for prime nos

# x = int(input())
# f=False
# if x == 1:
#     print("Not prime")
# elif x > 0:
#     for i in range(2, x):
#         if x%i==0:
#             f = True
#     if f==True:
#         print("Not prime")
#     else:
#         print("Is prime")
# else:
#     print("enter valid positive number")


# pw = input()
# if 6<=len(pw)<=16:
#     lower_case = 0
#     upper_case = 0
#     num = 0
#     spec_char = 0
#     for c in pw:
#         if 97<=ord(c)<=122:
#             lower_case+=1
#         elif 65<=ord(c)<=90:
#             upper_case+=1
#         elif c in ['$', '@', '#']:
#             spec_char+=1
#         elif 0<=int(c)<=9:
#             num+=1        
#     if lower_case >= 1 and upper_case >= 1 and num >= 1 and spec_char >= 1:
#         print("Password is strong")
#     else:
#         print("Enter a valid password")    
# else:
#     print("Enter a valid password")


# p = 0
# n = int(input())

# for i in range(1, n+1):
#     x="1"*i
#     m = x
#     m = int(m)
#     p = m + p
# print(p)

# x = int(input(), 2) 
# x = x+1

# b = bin(x)
# b = b.replace("0b", "")
# b_comp=""
# for i in range(0,len(b)):
#     if b[i] == "1":
#         b_comp = b_comp + "0"
#     elif b[i] == "0":
#         b_comp = b_comp + "1"
#     else:
#         pass

# print(b_comp)



# n = int(input())

# for i in range(1,n+1):
#     print(str(i)*(n+1-i))

# counter=0
# for i in range(1,8):
#     for j in range(0,i):
#         print(chr(65+counter), end=" ")
#         counter +=1
#     print("")



# rows = int(input())
# for i in range(1, rows+1):
#     C = 1
#     for j in range(1, i+1):
#         print(C, end = " ")

#         C = int(C*(i - j)/j)
#     print(" ")

"""
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555

[5, 4, 3, 2, 1]
"""


# n = int(input())
# myList=[]
# for i in range(1, n+1):
#     myList.append(i)
# myList.sort(reverse=True)

# myListrev = []
# for i in range(1, n+1):
#     myListrev.append(i)

# myListstr = ""
# myListrevstr = ""

# for i in myList:
#     myListstr+= str(i)
# for i in myListrev:
#     myListrevstr+= str(i)

# for j in range(1, n+1):
#     for k in range(0,j):
        
#         print(str(myList[k]), end="")


#         # print(str(myList[k]))
#     print(myListrevstr[n-j-2:], end="")
    
#     print()



# def fun1(a,b):
#     s=a+b
#     print(s)
# fun1(2,3)

# x = int(input())
# x_bin = bin(x)
# x_bin = x_bin.replace("0b", "")
# print(int(x_bin))


# mini=1
# e=2.7182
# d=e**(10-(1.05*mini))
# s=e**(1+(1.06*mini))
# if d==s:
#     print(mini)

# while s<d:
#     mini=mini+(0.05*mini)
#     d=e**(10-(1.05*mini))
#     s=e**(1+(1.06*mini))
#     if s==d:
#         break
# if s==d:
#     print("Equilibrium reaches at the price",mini,"at the value of",d)
# else:
#     print("there is no soln")
#     print("nearest price to equilibrium is",mini,"and the range of equilibrium is from",d,"to",s)


# if d<s:
#     while d<=s:
#         d=e**(10-(1.05*mini))
#         s=e**(1+(1.06*mini))
#         mini=mini+(0.5*mini)
#     print(mini)


# print(int(0.8))

# x = 'b a n a n a'
# print(x.replace('a','z')


'''
code for any number system conversion from decimal
'''''

# n, k = int(input()), int(input())
# string=""
# while n>=k:
#     string=str(n%k)+string
#     n=n//k
#     if n<k:
#         string=str(n)+string
# print(int(string))


# string = "yo mama"
# print(string[::-1])

# list = [1,2,3,4,5,6,7,8,9,10]
# # print(list[-2:-5:-1])

# del list[9]
# print(list)

# l1 = ["teri", "ma"]
# l2 = ["ka", "bhosda"]
# l3 = l1+l2
# print(l3)


# lst = [4,5,6,1,2,3,9,8,7]
# lst.sort()
# print(lst)

# n = 5
# m = []
# for i in range(n):
#     m.append([0 for n in range(n)])
#     for j in range(n):
#         if i==j:
#             m[i][j]=0
#         elif i<j:
#             m[i][j]=1
#         elif i>j:
#             m[i][j]=-1

# for i in range(len(m)):
#     for j in range(len(m[i])):
#         print(m[i][j], end=' ')
#     print()


# string = "             i love yuo bitch"
# print(string.strip())



# dicc = {1:"shjdb",
#         'hbsd': 23}

# print(dicc[1])


# import requests
# resp = requests.get('http://api.github.com/SakshxmSingh/followers')
# print(resp.text)

# menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

# # Print the menu
# print("Menu:")
# for i, item in enumerate(menu):
#     name, price = item
#     print(f"{i+1}. {name}: Rs {price}")

# # Initialize the order list and the total bill
# order = []
# total_bill = 0

# while True:
#     # Get the input from the user
#     user_input = input("Enter your order (item number and quantity): ")
    
#     # Check if the input is empty (end of order)
#     if not user_input:
#         break
    
#     # Split the input into item number and quantity
#     item_number, quantity = user_input.split()
#     item_number = int(item_number) - 1
#     quantity = int(quantity)
    
#     # Get the item name and price
#     item_name, item_price = menu[item_number]
    
#     # Add the item to the order list and add the price to the total bill
#     order.append((item_name, quantity, item_price * quantity))
#     total_bill += item_price * quantity

# # Print the order
# print("\nOrder:")
# for item in order:
#     name, quantity, price = item
#     print(f"{name}, {quantity}, Rs {price}")
    
# # Print the total bill
# print(f"\nTOTAL, {len(order)} items, Rs {total_bill}")

# def shortest_palindromic_string(s):
#   result = s
#   i = 0
#   while True:
#     if result == result[::-1]:
#       print(result)
#       return
#     else:
#         result = s[i] + result
#         i += 1

# s = input()
# print(shortest_palindromic_string(s))

# f = open('CSE101 - IP/bs.txt','a')
# for i in range(0,60):
#   f.write(str(i)+'\n')
  

# file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/MTH100 A1/matrix.txt", "r+")
# mtx = [list(map(float,i.split())) for i in file]

# for k in range(len(mtx)-1):
#   for i in range(k+1,len(mtx)):
#     mult = mtx[i][k]/mtx[k][k]
#     for j in range(k+1,len(mtx)):
#       mtx[i][j] = mtx[i][j] - mult*mtx[k][j]
    
# print(mtx)


# def fib(n):
#   if n==0:
#     return 0
#   elif n==1 or n==2:
#     return 1

#   return fib(n-1) + fib(n-2)

# print(fib(6))

# sum=0
# init = [0,1]
# for i in range(10):
#   init.append(init[len(init)-1]+init[len(init)-2])
# for j in init:
#   print(j)


# def sum(n, i=0):
#   n = str(n)
#   if i==len(n)-1:
#     return int(n[i])
#   return int(n[i])+sum(n,i+1)
# print(sum(458))

# def pow(x,y):
#   i = 1
#   if y == 0:
#     return 1

# import math

# file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/MTH100 A1/matrix.txt", "r+")
# mtx = [list(map(float,i.split())) for i in file]

# rows = len(mtx)
# cols = len(mtx[0])

# def swap(r1,r2):
#         r1, r2 = r2, r1
#         return r1, r2

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

# def forward_el(matrix):
#     global rows, cols

#     i = 0
#     for j in range(cols):
#         if i >= rows:
#             break
        
#         for k in range(i, rows):
#             if matrix[k][j] != 0:
#                 matrix[i], matrix[k] = swap(matrix[i], matrix[k])
#                 break
        
#         if matrix[i][j] == 0:
#             continue
        
#         pivot = matrix[i][j]
#         for k in range(i+1, rows):
#             scale = matrix[k][j] / pivot
#             for l in range(j, cols):
#                 matrix[k][l] -= scale * matrix[i][l]
#         i += 1

#     for x in range(rows):
#         for y in range(cols):
#             matrix[x][y]=round(matrix[x][y],3)

#     for i in range(rows):
#         matrix[i] = pivot_divide(matrix[i])
    
#     for x in range(rows):
#         for y in range(cols):
#             matrix[x][y]=round(matrix[x][y],3)

#     return matrix

# def back_sub(matrix):
#     global rows, cols
#     if cols>=rows:
#         for i in range(1,rows):
#             if matrix[i][i]==1:
#                 for j in range(i):
#                     if matrix[j][i]==0:
#                         pass
#                     else:
#                         matrix[j] = [matrix[j][k] - matrix[j][i]*matrix[i][k] for k in range(cols)]
#             elif matrix[i][i]==0:
#                 for k in range(i,cols):
#                     if matrix[i][k]==1:
#                         for j in range(i):
#                             if matrix[j][k]==0:
#                                 pass
#                             else:
#                                 matrix[j] = [matrix[j][x] - matrix[j][k]*matrix[i][x] for x in range(cols)]
#     else:
#         for i in range(1,cols):
#             if matrix[i][i]==1:
#                 for j in range(i):
#                     if matrix[j][i]==0:
#                         pass
#                     else:
#                         matrix[j] = [matrix[j][k] - matrix[j][i]*matrix[i][k] for k in range(cols)]
#             elif matrix[i][i]==0:
#                 for k in range(i,cols):
#                     if matrix[i][k]==1:
#                         for j in range(i):
#                             if matrix[j][k]==0:
#                                 pass
#                             else:
#                                 matrix[j] = [matrix[j][x] - matrix[j][k]*matrix[i][x] for x in range(cols)]    

#     for x in range(rows):
#         for y in range(cols):
#             matrix[x][y]=round(matrix[x][y],3)
#             if matrix[x][y] == -0:
#                 matrix[x][y] = int(matrix[x][y])
#             elif math.modf(matrix[x][y])[0] == 0:
#                 matrix[x][y] = int(matrix[x][y])

#     return matrix

# def parm(matrix):
#     global rows, cols, pivot_list, col_list, non_pivots
#     pivot_list = []
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j]!=0:
#                 pivot_list.append(j)
#                 break
    
#     col_list = [i for i in range(cols)]
#     non_pivots = [i for i in col_list if i not in pivot_list]

#     for i in non_pivots:
#         print('x{} is free'.format(i+1))
#     print("----------------------------------------------")

#     trans_mtx = list(zip(*matrix))
#     print(trans_mtx)
#     vectors = []
#     for i in non_pivots:
#         temp = [float(0)]*len(matrix[0])
#         for j in range(len(temp)):
#             if j == i: temp[j] = 1

#         for j in range(len(trans_mtx)):
#             if j == i:
#                 print(trans_mtx[j])
#                 for k in range(len(trans_mtx[j])):
#                     if trans_mtx[j][k] != float(0):
#                         temp[pivot_list[k]] = -trans_mtx[j][k]
#         vectors.append(temp)
#     if len(vectors)==0:
#         print("Only trivial solution exists")   
#     else:
#         print("The parametric form is:\nX = ",end="")
#         for i in range(len(vectors)):
#             print(f"x{non_pivots[i]+1}{vectors[i]}", end = " + ") if i != (len(vectors)-1) else print(f"x{non_pivots[i]+1}{vectors[i]}")
#     print("----------------------------------------------")
    
# ef_mtx = forward_el(mtx)
# rref_mtx = back_sub(ef_mtx)

# print("----------------------------------------------\nThe RREF matrix is:\n----------------------------------------------")
# for i in rref_mtx:
#     print("|",end=" ")
#     for j in i:
#         print(j,end="\t")
#     print("|")
# print("----------------------------------------------")

# parm(rref_mtx)


# import matplotlib.pyplot as plt
# # Create some data
# X = [1, 2, 3, 4, 5]
# Y = [2, 4, 6, 8, 10]
# # Create a basic line plot
# plt.plot (X, Y)
# # Show the plot
# plt.show ()



# import numpy

# n = int(input())
# p = int(input())
# k = int(input())
# m = int(input())

# mat1 = []
# for i in range(n):
#     temp = [int(i) for i in list(input().split())]
#     mat1.append(temp)
    
# mat2 = []
# for i in range(k):
#     temp = [int(i) for i in list(input().split())]
#     mat2.append(temp)
    
# np_mat1 = numpy.array(mat1)
# np_mat2 = numpy.array(mat2)

# try:
#     mult = numpy.dot(np_mat1, np_mat2)
#     for i in range(len(mult)):
#         for j in range(len(mult[0])):
#             print(float(mult[i][j]), end=' ')
#         print()
# except:
#     print("Dimensions of matrices are not compatible")




# import matplotlib.pyplot as mpt

# y_coords = list(map(int,input().split()))
# x_coords = [i+1 for i in range(len(y_coords))]
# y_mean = float(sum(y_coords)/len(y_coords))

# mpt.plot(x_coords,y_coords, color="blue")
# mpt.axhline(y_mean, linestyle='--', color="red")
# mpt.show()


# import math

# coeff = list(map(int,input().split()))

# def quadratic_check(coef):
#     assert len(coef) == 3, "Type-1"
#     assert (coef[1])**2 - 4*coef[0]*coef[2] >= 0, "Type-2"
    
#     r1, r2 = (-coef[1] + math.sqrt((coef[1])**2 - 4*coef[0]*coef[2]))/2*coef[2] , (-coef[1] - math.sqrt((coef[1])**2 - 4*coef[0]*coef[2]))/2*coef[2]
        
#     print(r1, r2)
#     assert max(r1,r2)%min(r1,r2)==0, "Type-3"
    
#     print(True)
    
# try:
#     quadratic_check(coeff)
# except AssertionError:
#     print(False)

