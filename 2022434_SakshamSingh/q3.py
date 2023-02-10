n = int(input("Enter n: "))

odd_nos = [i for i in range(2,10) if i%2==1]

# for j in odd_nos:
#     ans = [i for i in range(1,n) if i%j==0]
#     ans = set(ans)
# print(ans)

ans = []
for j in odd_nos:
    ans += [i for i in range(1,n) if i%j==0]

ans = set(ans)
print(ans)