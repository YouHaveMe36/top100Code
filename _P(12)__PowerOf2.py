
# from typing import Counter
# r = 46
# c = Counter([int(i) for i in str(r)])
# print(type(c))
# n,i = 0,0
# while(n<=10**9):
#     n = 2**i
#     d = Counter([int(i)for i in str(n)])
#     if(d==c):
#         print(True)
#         print(d)
#         break
#     i+=1
# print(c)

# r = 46
# d = {}
# for i in str(r):
#     i = int(i)
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# r,n = 0,0
# while(n<=2**9):
#     n = 2*r
#     s = {}
#     for i in str(r):
#         i = int(i)
#         if i not in s:
#             s[i]=1
#         else:
#             s[i]+=1
#     if(s==d):
#         print(True)
#         print(s)
#         print(d)
#         break
#     else:
#         r+=1

s = "ab"
p = ".*"

if(len(s)==len(p)):
    for i in range(len(s)):
        if(s[i]==p[i] or p[i]=="."):
            if(s[i+1]==p[i+1] or p[i]=="*" or p[i]=="."):
                print(True)
            else:
                print(False)
