







class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [9]:
            return [1, 0]
        elif digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            n = len(digits) - 1
            while digits[n] == 9:
                digits[n] = 0
                n = n - 1
            if n + 1 > 0:
               digits[n] += 1
               return digits
            elif n + 1 == 0:
                digits.insert(0, 1)
                return digits


jiayi = Solution()
result = jiayi.plusOne([9, 9, 9, 9, 9])
print(result)








# c = 1
# new_digits = []
# for i in reversed(digits):
#     sum1 = i + c
#     new_digits.append(int(sum1 % 10))
#     c = int(sum1 / 10)
# if c != 0:
#     new_digits.append(c)
# new_digits.reverse()
# return new_digits
