# def addition(a,b):
#     print(a+b)
#     return a+b

# addition(5,6)


# n = int(input())

# for i in range(0, n):
#     print("*"*(n-i)+(" "*2*i)+"*"*(n-i))
# for i in range(1, n+1):
#     print("*"*(i)+(" "*(2*(n-i))+"*"*(i)))

# def f(x):
#     y = (x**3+2)/(x**2+1)
#     return y 

# def integration(l,u,dx):
#     x=l
#     area = 0
#     while l<=x<=u:
#         area = area + f(x)*dx
#         x = x + dx
#     print(area)


# ll = int(input())
# ul = int(input())

# integration(ll,ul,dx=0.0001)

"""
    *
   * *
  * * *
 * * * *
* * * * *

"""


n = int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"* "*(i-1)+"*")


