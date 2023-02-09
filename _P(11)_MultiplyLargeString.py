num1 = "456"
num2 = "123"
res1, res2 = 0, 0 
for d in num1:
    res1 = res1 * 10 + (ord(d) - ord('0'))
for d in num2:
    res2 = res2 * 10 + (ord(d) - ord('0'))
print(str(res1 * res2))