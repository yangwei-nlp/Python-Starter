# 法一，正向思路：逐个步骤逐个步骤的判断。唯一可能难点就在如何对连续的长度进行计算
# 我这里用的是末尾添加0，然后循环法判断每种二进制码，但是估计会超时
# 因为本来每种二进制码有联系的，但是这里没有用到这个关系
class Solution:
    def findLatestStep(self, arr, m):
        init_code = "0"*len(arr)
        latest_step = -2
        for step, idx in enumerate(arr):
            init_code = init_code[:idx-1] + '1' + init_code[idx:]
            if m in self.count_one(init_code):
                if step > latest_step:
                    latest_step = step
        return latest_step+1

    
    def count_one(self, bin_code):
        bin_code += '0'
        ret = []
        i = 0
        tmp = ""
        while i < len(bin_code):
            if bin_code[i] == '0':
                if tmp != "":
                    ret.append(len(tmp))
                    tmp = ""
            else:
                tmp += "1"
            i += 1
        return ret


s = Solution()
arr = list(range(100000000))
m = 100000
print(s.findLatestStep(arr, m))

# s.count_one("00101")