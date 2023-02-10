def pword_check(string):
    spec = ['@','#','4','%','&']
    f = True
    count_spec = 0
    count_caps = 0
    count_digs = 0
    count_lows = 0
    if len(string)<8:
        f = False
    for i in string:
        if i in spec:
            count_spec+=1
        elif i.isupper():
            count_caps+=1
        elif i.islower():
            count_lows+=1
        elif i.isdigit():
            count_digs+=1
    if count_digs<1 or count_caps<1 or count_lows<1 or count_spec<1:
        f = False

    return f

print(pword_check(input("Enter pword: ")))