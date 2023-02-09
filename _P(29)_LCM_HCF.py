#relation:
"""This relation only hold true for only two number."""
#LCM * HCF = NUM1*NUM2
# num1 = 5
# num2 = 10
# hcf = 1
# lcm = 1
# for i in range(1,min(num1,num2)+1):
#     if (num1%i==0 and num2%i==0):
#         hcf = i
#     lcm = (num1*num2)//hcf
# print(hcf)
# print(lcm)


"""Question:find the lcm in the array form any index value."""
# arr = [12,15,75]
# def hcf(num1,num2):
#     if(num2==0):
#         return num1
#     else:
#         return hcf(num2,num1%num2)
# def lcm(arr,idx):
#     if (idx == len(arr)-1):
#         return arr[idx]
#     a = arr[idx]
#     b = lcm(arr, idx+1)
#     return int(a*b//hcf(a,b))
# print(lcm(arr,0))


