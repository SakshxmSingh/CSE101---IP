# op = input()
# a = float(input())
# b = float(input())

# if op == "+":
#     print(a+b)
# elif op == "-":
#     print(a-b)
# elif op == "*":
#     print(a*b)
# elif op == "/":
#     print(a/b)







# n = int(input())
# list = []
# cost = 0
# for i in range(1, n+1):
#     list.append(int(input()))

# for j in list:
#     if 1<=j<=5:
#         cost = cost + 5
#     elif 6<=j<=12:
#         cost = cost + 10
#     else:
#         cost = cost + 20
# print(cost)







# n = int(input())
# list = []
# for i in range(1, n+1):
#     list.append(int(input()))
    
# f = True    
    
# for j in list:
#     if list.count(j)>=2:
#         break
#     else:
#         f=False

# print(f)






# a = int(input())
# b = int(input())

# n = 0
# for i in range(a, b+1):
#     for j in range(2, i):
#         if i%j==0:
#             break
#     else:
#         n+=1
# print(n)







# def pangramcheck(str):
#     alphabets="abcdefghijklmnopqrstuwxyz"
#     for i in alphabets:
#         if i not in str:
#             return False
#     else:
#         return True

# string = input()

# print(pangramcheck(string))







# n = int(input())
# list = []
# answer = []
# for i in range(1, n+1):
#     list.append(int(input()))

# target = int(input())

# f=False

# for j in list:
#     x = target - j
#     for k in list:
#         if x == k and list.index(k)!=list.index(j):
#             answer.append(list.index(k))
#             answer.append(list.index(j))
#             f=True
#     if f:
#         break

# answer.sort(reverse=True)
# for y in answer:
#     print(y)







# a = int(input())
# b = int(input())

# factors_a = []
# factors_b = []
# common_factors = []
# for i in range(2,a+1):
#     if a%i==0:
#         factors_a.append(i)

# for j in range(2,b+1):
#     if b%j==0:
#         factors_b.append(j)

# for x in factors_a:
#     if x in factors_b:
#         common_factors.append(x)

# for y in factors_b:
#     if y in factors_a:
#         common_factors.append(y)

# common_factors.sort()

# print(common_factors[len(common_factors)-1])






# y = list(input().split())
# print(len(y))
