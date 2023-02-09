##Recursive Code   ##T.C = O(n/2) S.C = O(n/2)
def pallandrom(i,s):
    if(i>=len(s)//2):
        return True
    if(s[i]==s[len(s)-i-1]):
        return pallandrom(i+1,s)
    return False
s = "madam"
obj = pallandrom(0,s)
print(obj)



##Iterative Code
def p(i,s):
    while(i<=len(s)//2):
        if(s[i]!=s[len(s)-i-1]):
            return False
        else:
            i=i+1
    return True

s = "madam"
obj  = p(0,s)
print(obj)

def pd(s):
    l = len(s)
    for i in range(l//2):
        if (s[i]==s[l-i-1]):
            continue
        else:
            return False
    return True

obj = pd("maoram")
print(obj)
        