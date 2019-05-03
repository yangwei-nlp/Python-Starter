class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 这种解法应该是回溯法，深度优先搜索
        if len(digits) == 0:
            return []
        num_dict = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl',
                    '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        base = list(num_dict[digits[0]])
        if len(digits) == 1:
            return base
        output = []
        for i in range(1, len(digits)):
            output = []
            for item in num_dict[digits[i]]:
                for base_item in base:
                    output.append(base_item+item)
            base = output
        return output

s = Solution()
print(s.letterCombinations("23"))


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 网上的递归解法，思路还行
        # 创建字母对应的字符列表的字典
        dic = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z'],
               }
        # 存储结果的数组
        ret_str = []
        if len(digits) == 0: return []
        # 递归出口，当递归到最后一个数的时候result拿到结果进行for循环遍历
        if len(digits) == 1:
            return dic[int(digits[0])]
        # 递归调用
        result = self.letterCombinations(digits[1:])
        # result是一个数组列表，遍历后字符串操作，加入列表
        for r in result:
            for j in dic[int(digits[0])]:
                ret_str.append(j + r)
        return ret_str

class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        strs = [dic[i] for i in digits]
        stack = [ch for ch in strs[0]]
        for i in range(1,len(strs)):
            iters = len(stack)
            for _ in range(iters):
                temp = stack.pop(0)
                for ch in strs[i]:
                    stack.append(temp+ch)
        return stack