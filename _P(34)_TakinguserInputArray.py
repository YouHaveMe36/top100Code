#Binary search with user Input array
nums = int(input("Enter the no. of element :-"))
arr = list(map(int,input("Enter the element :- ").strip().split()))[:nums]
search_Item = int(input("Enter the Item you want to seach :- "))

def _binary_Search(search_Item,arr):
    start_index = 0
    end_index = len(arr)-1
    while (end_index>=start_index):
        mid = start_index + (end_index-start_index)//2
        if(arr[mid]==search_Item):
            return mid
        elif (arr[mid]>search_Item):
            start_index = mid+1
        else:
            end_index = mid-1
    return -1
check = _binary_Search(search_Item,arr)
print(check)


       

    

    