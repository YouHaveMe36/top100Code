""" Method 1:"""
num = 6 
sum=0
temp=num
base=1
while(temp):
    digit=temp%2
    sum+=digit*base
    base*=10
    temp//=2
print(sum)

""" Method 2: """

x = 5
y = bin(x).replace("0b","")
y = y[::-1]
print(int(y,2))
