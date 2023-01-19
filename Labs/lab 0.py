n = int(input())
y = list(map(int, input().split()))


def even(list):
    for i in list:
        if i %2 != 0:
            list.remove(i)   

def odd(list):
    for i in list:
        if i %2 != 1:
            list.remove(i) 

e = list(map(even, y))
f = list(map(odd, y))

print(e)
print(f)
