def subset(i,arr,ss):
    if(i==len(arr)):
        print(ss)
        return
    else:
        subsequence.append(arr[i])
        subset(i+1,arr,subsequence)
        subsequence.pop()
        subset(i+1,arr,subsequence)
    return subsequence
        