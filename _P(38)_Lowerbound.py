##lowerbound means that the next element that is greater then or equal to target element

#Method1:-
# arr = [1,3,5,5,7,9,10]
# start = 0
# end = len(arr)-1
# x = 4
# lb = -1
# while(start<=end):
#     mid = start + (end-start)//2
#     if(arr[mid]==x):
#         lb = x
#         print(lb)
#         break
#     elif(arr[mid]>x):
#         end = mid-1
#     else:
#         start = mid+1
# if(start==len(arr)):
#     print(-1)
# else:
#     print(arr[start])


#Method 2:-
arr = [1,3,5,5,5,5,7,9,10]
start = 0
end = len(arr)-1
x = 6   
lb = len(arr)       
while(start<=end):
    mid = start + (end-start)//2
    if(arr[mid]>=x):
        lb=mid
        end = mid-1
    else:
        start = mid+1
if(lb==len(arr)):
    print(-1)
else:
    print(lb)    

