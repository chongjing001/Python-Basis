

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = nums
        nums1 = list(set(nums))
        nums1.sort(key=nums.index)
        nums = nums1
        return nums

paixu = Solution()
result = paixu.removeDuplicates([1, 1, 2])
print(result)













