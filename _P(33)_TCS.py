""" Question:print the string if the character is vowel the do not change it else swap it to it's next immediate element.
         if character is z then swap it with b . if character is b then swap it with c. if character is a the do not change any thing"""

s = "zrast"
c = "bcdfghjklmnpqrstvwxy"
ans = ""
for i in range(len(s)):
    if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
        ans+=s[i]
    else:
        if(s[i]=="z"):
            ans+="b"
        else:
            if(s[i] in c):
                t = c.find(s[i])
                p = c[t]
                q = c[t+1]
            p,q = q,p
            ans+=p
print(ans)