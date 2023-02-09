nums1 = 10
nums = str(nums1)
d = int(nums,8)
print(d)


num = 101
binary_val = num
decimal_val = 0
b = 1
while(num!=0):
    rem = num%10
    decimal_val+=rem*b
    num = num//10
    b = b*2
print(decimal_val)