

#  超时
# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         nums1 = []
#         if nums is []:
#             return False
#         for i in nums:
#             if i not in nums1:
#                 nums1.append(i)
#         if len(nums1) < len(nums):
#                 return True
#         else:
#                 return False
#
# repeat = Solution()
# result = repeat.containsDuplicate([2, 1])
# print(result)



class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is []:
            return False
        len1 = len(nums)
        nums1 = list(set(nums))
        if len(nums1) < len1:
            return True
        else:
            return False
repeat = Solution()
result = repeat.containsDuplicate([1, 2, 1])
print(result)

