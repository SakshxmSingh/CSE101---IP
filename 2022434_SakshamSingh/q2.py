salaries = [30, 50, 20, 15, 80, 70, 40, 30]

def mafths(lst):
    lst.sort()
    # print(lst)
    median = 0
    if len(lst)%2==0:
        median = (lst[int(len(lst)/2)-1] + lst[int(len(lst)/2)])/2
    else:
        median = lst[len(lst)//2]

    sum_bel = 0
    n_bel = 0
    for i in lst:
        if i<median:
            sum_bel+=i
            n_bel+=1
    avg_bel = sum_bel/n_bel

    sum_up = 0
    n_up = 0
    for i in lst:
        if i>=median:
            sum_up+=i
            n_up+=1
    avg_up = sum_up/n_up

    return median , avg_bel , avg_up

print(mafths(salaries))

