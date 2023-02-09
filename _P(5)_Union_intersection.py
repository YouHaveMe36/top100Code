# nums1 = [1,23,2]
# nums2 = [4,5,6]
# #for union of two set distinct element only this code cannot handel duplicates 
# def union(nums1,nums2):
#     ans = []
#     i = 0
#     j = 0
#     while(i<len(nums1) and j<len(nums2)):
#         if(nums1[i]<nums2[j]):
#             ans.append(nums2[i])
#             i+=1
#         elif(nums1[i]>nums2[j]):
#             ans.append(nums1[j])
#             j+=1
#         else:
#             ans.append(nums1[i])
#             i+=1
#             j+=1
#     while(i<len(nums1)):
#         ans.append(nums1[i])
#         i+=1
#     while(j<len(nums2)):
#         ans.append(nums2[j])
#         j+=1
#     return ans
# obj = union(nums1,nums2)
# print(obj)
        