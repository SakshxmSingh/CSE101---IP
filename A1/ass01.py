#--------------ques01------------------

n = int(input())
list_tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
list_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
list_ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
if 0<n<100:
    if n<10:
        print(list_ones[n])
    elif 10<=n<20:
        print(list_teens[int(str(n)[1])])
    elif n>=20:
        print(list_tens[int(str(n)[0])], list_ones[int(str(n)[1])])


#--------------ques02-------------------

#--------------ques03-------------------
x0 = int(input())
y0 = int(input())

dist = []
n = 0
s = 0
e = 0
w = 0

f = True
while f:
    x = int(input())
    if x>0:
        dist.append(x)
    else:
        f = False

for i in dist:
    if i<=25:
        n+=i
    elif 26<=i<=50:
        s+=i
    elif 51<=i<=75:
        e+=i
    elif i>=76:
        w+=i

x = e - w + x0
y = n - s + y0

print("("+str(x)+","+str(y)+")")                    #co-ordinates
print(n+s+e+w)                                      #distance
print(((x-x0)**2 + (y-y0)**2)**(1/2))               #displacement



# #--------------ques04-------------------
import math
def integration(f,l,u,dx):
    area = 0
    x = l
    while x<=u:
        area = area + (1/2)*(f(x)+f(x+dx))*dx
        x+=dx
    print(area)

def func(x):
    y = 2000*math.log(140000/(140000-2100*x))-9.8*x
    return y

lower = int(input())
upper = int(input())

integration(func,lower,upper,dx=0.25)



#--------------ques05-------------------

#--------------ques06-------------------
n = int(input())
for i in range(1,n+1):
    print("*"*i+" "*(2*n-2*i)+"*"*i)
    

#--------------ques07-------------------
cost = int(input())
allowance = int(input())
sf = int(input())
rate = float(input())

savings = allowance*sf
account = 0
months = 0
while account <= cost:
    account+=savings
    account+=account*rate
    months+=1

print(months)
print(account-cost)



#--------------ques08-------------------
pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

