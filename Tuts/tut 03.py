# n= int(input())
# if n >= 0:
#     print(str(n)+" is positive")
# else:
#     print(str(n)+" is negative")

# n = int(input())

# if 81<=n<=100:
#     print('a')
# elif 61<=n<=80:
#     print('b')
# elif 41<=n<=60:
#     print('c')
# elif 21<=n<=40:
#     print('d')
# elif 0<=n<=20:
#     print('f')


# l = list(map(int, input().split()))
# for i in l:
#     print(i)

import math
a = int(input())
a = (a**(1/2))
t = math.modf(a)
if t[0]!=0:
    print("NO")
else:
    print("YES")

