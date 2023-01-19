"""
fs = [0, 0, 1]

while len(fs) <= 50:
    fs.append(fs[len(fs) - 2] + fs[len(fs) - 1])

n = int(input())
print(fs[n]) 

-----------------------------------------


ih = int(input())
iw = int(input())
tw = int(input())
th = int(input())

bh = int(input())
bw = int(input())


for i in range (0,ih):
    print('*'*iw)
for i in range (0,th):
    print('*'*tw)
for i in range (0, bh):
    if (tw-bw)%2 == 0:
        print(" "*int(((tw-bw)/2))+"*"*bw)
    if (tw-bw)%2 != 0:
        print(" "*int(((tw-bw)/2).floor())+"*"*bw)


a = int(input())
b = int(input())

print(a & b)
print(a | b)

a = int(input())
a = format(a, 'b')
b = int(input())
b = format(b, 'b')

x = ''
y = ''
for i in range(1, len(a)+1):
    if int(a[i]) == 1 and a[i] == b[i]:
        x = x+'1'
    elif int(a[i]) == 1 or int(b[i]) == 1:
        y = y+'1'
    else:
        x = x+'0'
        y = y+'0'

print(int(x, 2))
print(int(y, 2))

"""

