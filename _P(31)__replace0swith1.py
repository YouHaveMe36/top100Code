s = "Move#Hash#to#Front"
a = [i for i in s]
r = a.count("#")    
n = []
for i in a:
    if i=="#":
        continue
    else:
        n.append(i)
k = ""
for i in n:
    k +=i
k = "#"*r + k
print(k)
s=input()
x=s.count("#")
s=s.replace("#","")
print("#"*x+s)





    
# obj = Solution()
# print(obj.search([4,5,6,7,0,1,2],0))








arr = [2,3,3,2]
val = 2
for i in arr:
    if i==val:
        arr.remove(i)
    else:
        continue
print(arr)
            