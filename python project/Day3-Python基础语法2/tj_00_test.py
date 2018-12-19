

#
# x = 51561456156
# x = str(x)
# x = list(x)
# print(x)
#
# a = "1231556"
# print(a[::-1])
def reverse_num():
    x = input("请输入要反转的数字")
    if x == "0":
        return x
    elif int(x) > 0:
        return x[::-1]
    else:
        x = -int(x)
        x = str(x)
        x = x[::-1]
        return -int(x)

# new_x = reverse_num()
# print(new_x)

print(2**31)
print(-2**31)





class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0 and x < 2**31:
            x = str(x)
            x = x[::-1]
            if int(x) > 2**31:
                return 0
            else:
                return int(x)
        elif x < 0 and x >= -(2**31):
            x = -x
            x = str(x)
            x = x[::-1]
            if -int(x) < -(2**31):
                return 0
            else:
                return -int(x)
        else:
            return 0
reverse_num = Solution()
result = reverse_num.reverse(1534236469)
print(result)


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # if int(a) and int(b) is bin:
        #
        #     result_bin = 0b(int(a)) + 0b(int(b))
        #     return str(bin(result_bin))


abc = 0b10101 + 0b10101
print(bin(abc))


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # for j,k in a,b:
        #     if j and k in ["0","1"]:
        #         result_bin = 0bint(a) + 0bint(b)
        #         return str(bin(result_bin))



a = "101010"
l = "1110101"

# help(int)
num = int(a, base=2)
print(num)
print(bin(42))

a = int('00111000', 2)
b = int('10000010', 2)
print (bin(a ^ b))

# 设x 是一个整数（16位）.若要通过x|y使x低度8位置1，高8位不变，则y的二进制数是