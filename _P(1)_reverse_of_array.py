# def reverse(num):
#     startInd = 0
#     endInd = len(num)-1
    
    
#     while(startInd < endInd):
#         num[startInd],num[endInd] = num[endInd],num[startInd]
        
#         startInd = startInd + 1
#         endInd = endInd -1
    
    
# if __name__=='__main__':
#     n =  [10,20,30,40,50]
#     reverse(n)
#     print(n)






class Solution:
    def intersection(self,nums1,nums2):
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        startInd = 0
        out = []
        Len1 = len(nums1)
        Len2 = len(nums2)
        if(Len2>=Len1):
            while(startInd<=Len1-1):
                if nums1[startInd] in nums2:
                    out.append(nums1[startInd])
                startInd +=1
        if(Len1>=Len2):
            while(startInd<=Len2-1):
                if nums2[startInd] in nums1:
                    out.append(nums2[startInd])
                startInd +=1
        return out
    
    
obj = Solution()
nums1 =[2,6,2,9,1]
nums2 = [7,1]
print(obj.intersection(nums1,nums2))