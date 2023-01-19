# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(int(input()))
    
# odd_nums = [i for i in nums if i%2==1]
# print(len(odd_nums))

# even_nums = [i for i in nums if i%2==0]
# print(len(even_nums))
                
# pos_nums = [i for i in nums if i>0]
# print(len(pos_nums))
                
# neg_nums = [i for i in nums if i<0]
# print(len(neg_nums))    
                
# zeros = [i for i in nums if i==0]
# print(len(zeros))





# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(int(input()))
    
# unique_nums = []
# for i in nums:
#     if i not in unique_nums:
#         unique_nums.append(i)

# print(unique_nums)





n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    
def sum(list):
    sum = 0
    for i in list:
        sum+=i
    return sum

sums=[]
subarray = []
for i in range(len(nums)):
    for k in range(len(nums)):
        for j in range(i,k):
            subarray.append(nums[j])
        sums.append(sum(subarray))
        subarray = []
        
for i in range(len(nums)):
    for j in range(i,len(nums)):
        subarray.append(nums[j])
    sums.append(sum(subarray))
    subarray = []
    
# print(max(sums))





# n = int(input())

# string = " "*(n-1)+"*" 
# x = list(string)
# for i in range(n):
#     x[n-1-i]="*"
#     print("".join(x))
#     x = list(string)

# string_rev = " "*(n-2)+"*" 
# for i in range(n-1):
#     x[i+1]="*"
#     print("".join(x))
#     x = list(string)





# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(int(input()))
    
# diff = []
# for i in range(n):
#     for j in range(i, n):
#         x = nums[j]-nums[i]
#         diff.append(x)

# print(max(diff))





# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(int(input()))

# volumes = []  
# for i in range(1, n+1):
#     for j in range(i,n+1):
#         x = abs(i-j)*min(nums[j-1],nums[i-1])
#         volumes.append(x)
        
# print(max(volumes))






# n = int(input())
# x = "<> "
# for i in range(1,n+1):
#     print(x*i+"   "*(2*n-2*i)+x*i)
# for i in range(0,n+1):
#     print(x*(n-i)+"   "*(2*i)+x*(n-i))





# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(int(input()))
# k = int(input())


# for i in range(k):
#     x = nums.pop(0)
#     nums.append(x)
    

# print(nums)