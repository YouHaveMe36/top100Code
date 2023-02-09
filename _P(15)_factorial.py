def facto(n):
    if(n<=1):
        return n
    else:
        return n*facto(n-1)

obj = facto(5)
print(obj)

##T.C = O(n)
##Space = O(n)