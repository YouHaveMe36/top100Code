arr = [1,5,7,9,3]
# def reverse(i,arr):
#     if(i>=len(arr)//2):
#         return
#     else:
#         arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
#         reverse(i+1,arr)
#     return arr

# obj = reverse(0,arr)
# print(obj)


# Iterative solution 

def reverse(arr):
    l = len(arr)
    for i in range(l//2):
        arr[i],arr[l-i-1] = arr[l-i-1],arr[i]
    return arr
obj = reverse(arr)
print(obj)
