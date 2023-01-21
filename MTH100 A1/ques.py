# Saksham Singh
# 2022434
# Section B,  Group 7
# MTH Assignment 01

file = open("/Users/saksham/Desktop/Programming/CSE101 - IP/MTH100 A1/matrix.txt", "r+")
mtx = [list(map(float,i.split())) for i in file]
print(mtx)

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


print(pivot_divide(mtx[0]))
