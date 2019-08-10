# 这是自己的方法，观察发现每层第一个元素和最后一个元素都是1
# 所以生成每层元素时首先定义所有元素均为1，但是还有别的方法
class Solution:
    def generate(self, numRows):
        result = []
        if numRows == 0:
            return result
        for i in range(1, numRows+1):
            # i 控制每一层
            temp = [1] * i
            if i > 2:
                for j in range(1, i-1):
                    temp[j] = result[i-1-1][j-1] + result[i-1-1][j]
            result.append(temp)
        return result

# s = Solution()
# print(s.generate(3))


# 方法2：
# 每层首尾新增元素0，按照规则来实现
class Solution2:
    def generate(self, numRows):
        if numRows == 0:
            return []
        last = [1]  # 上一层
        result = [last]
        i = 1
        while i < numRows:
            i += 1
            temp = [0] * i  # 当前层
            last = [0] + last + [0]  # 为上一层两端添加0
            for j in range(i):
                temp[j] = last[j] + last[j+1]
            last = temp
            result.append(temp)
        return result


# s2 = Solution2()
# print(s2.generate(3))


# 方法3：
# 利用一种技巧实现杨辉三角的计算原理
class Solution3:
    def generate(self, numRows):
        if not numRows:
            return []
        result = [[1]]
        for i in range(1, numRows):
            result.append(list(map(lambda x, y: x + y, [0] + result[-1], result[-1] + [0])))
        return result


s3 = Solution3()
print(s3.generate(3))
