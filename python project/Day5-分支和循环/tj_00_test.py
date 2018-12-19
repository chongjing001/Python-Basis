import re


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if re.search("^[A-Z]+$", word):
            return True
        elif re.search("^[a-z]+$", word):
            return True
        elif re.search("^[A-z]{1}[a-z]+$", word):
            return True
        else:
            return False
zimu = Solution()
result = zimu.detectCapitalUse("Flaaaazs")
print(result)