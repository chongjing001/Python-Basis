class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(0, len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a] + nums[b] == target and a != b:
                    return [a, b]


nums = [2, 7, 11, 15]
target = 9
answer = Solution()
list = answer.twoSum(nums, target)
print(list)





