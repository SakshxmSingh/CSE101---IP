lust = ['a','b','c','d','e']
def palindrome(lst):
    pal_lust = []
    for i in range(len(lst)):
        pal_lust.append(lst[i])
    for i in range(2,len(lst)+1):
        pal_lust.append(lst[-i])
    return pal_lust

print(palindrome(lust))
