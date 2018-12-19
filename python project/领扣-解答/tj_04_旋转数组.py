

# class Solution:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             # nums[i], nums[-1-i] = nums[-1-i], nums[i]
#             nums.insert(0, nums[-1])
#             nums.pop()
#
#         return nums
# rotate = Solution()
# result = rotate.rotate([1,2,3,45,9,79,7,45,14], 3)
# print(result)



class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len1 = len(nums)
        k %= len1
        nums.extend(nums[0:len1-k])
        del nums[0:len1-k]

        return nums
rotate = Solution()
result = rotate.rotate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 10)
print(result)













