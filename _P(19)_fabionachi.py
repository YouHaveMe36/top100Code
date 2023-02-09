def fabio(n):
    if(n<=1):
        return n
    else:
        # ans1 = fabio(n-2) this will also give the ans
        # ans2 = fabio(n-1)
        # return ans1+ans2
        return fabio(n-2)+fabio(n-1)
obj = fabio(6)
print(obj)

##T.C O(2^n)
##space = O(N)


# Iterative 
# def fab(n):
#     num1 = 0
#     num2 = 1
#     arr = ""
#     if(n==0):
#         return str(num1)
#     elif(n==1):
#         arr = str(num1)+" "+str(num2)
#         return arr
#     else:
#         arr = '0'
#         for i in range(n):
#             arr+=" "+str(num2)
#             nterm = num1+num2
#             num1,num2 = num2,nterm
#         return arr
# obj = fab(7)
# print(obj)
