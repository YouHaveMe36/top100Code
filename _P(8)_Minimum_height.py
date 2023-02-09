def getMinDiff( arr, n, k):
    arr.sort()
    if(len(arr)==1):
        return 0
    res = arr[n-1]-arr[0]
    for i in range(1,len(arr)):
        if(arr[i]-k<0):
            continue
        mxvalue = max(arr[i-1]+k,arr[n-1]-k)
        mivalue = min(arr[i]-k,arr[0]+k)
        res = min(res,mxvalue-mivalue)
    return res
obj = getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1],10,5)
print(obj)