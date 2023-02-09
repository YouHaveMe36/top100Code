name = "massalaii"
d = {}
for i in name:
    if i not in d:  
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if(d.get(i)==1):
        print(i)
        
        
