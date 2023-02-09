arr = [1,2,3,3,4,4,4,4,5,8,23,7]
finalAnswer = 0
def LastOccurence(arr,num):
    start1,end1,last = 0,len(arr)-1,0
    start2,end2,first = 0,len(arr)-1,0
    while(start1<=end1):
        mid = (start1+end1)//2
        if (arr[mid]==num):
            last = mid
            start1=mid+1
        elif(arr[mid]<num):
            start1 = mid+1
        else:
            end1 = mid-1
    while(start2<=end2):
        mid = (start2+end2)//2
        if (arr[mid]==num):
            first = mid
            end2=mid-1
        elif(arr[mid]<num):
            start2 = mid+1
        else:
            end2 = mid-1
    finalAns = (last-first+1)
    if(finalAns==1):
        return 0
    else:
        return finalAns

obj = LastOccurence(arr,3)
print(obj)
        