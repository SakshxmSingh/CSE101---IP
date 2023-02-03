import math

coeff = list(map(int,input().split()))

def quadratic_check(coef):
    assert len(coef) == 3, "Type-1"
    assert (coef[1])**2 - 4*coef[0]*coef[2] >= 0, "Type-2"
    
    r1, r2 = (-coef[1] + math.sqrt((coef[1])**2 - 4*coef[0]*coef[2]))/2*coef[2] , (-coef[1] - math.sqrt((coef[1])**2 - 4*coef[0]*coef[2]))/2*coef[2]
        
    assert max(r1,r2)%min(r1,r2)==0, "Type-3"
    
    print(True)
    
try:
    quadratic_check(coeff)
except AssertionError:
    print(False)

# try:
#     i = int(input("Enter a number greater than 6: "))
#     assert i>6 , 'Number not greater than 6'
#     print(i**2)
# except AssertionError:
#     print(i**3)
