# 法一，正向思路：逐个步骤逐个步骤的判断。唯一可能难点就在如何对连续的长度进行计算
# 我这里用的是末尾添加0，然后循环法判断每种二进制码，但是超时了
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


# s = Solution()
# arr = list(range(100000000))
# m = 100000
# print(s.findLatestStep(arr, m))

# s.count_one("00101")


# 法二，上面方法的超时原因在于：处理时没有利用上一步与这一步的关系，
# 认为其是独立的，没有利用前后依赖关系导致了复杂性
# 这里思路：
"""
每操作一次，新增的 1 可能会有如下三种情况：

1、左右都是 0。此时该位置作为 新增段独立存在。
2、仅有左边或者右边。此时该位置 会将某个旧段的长度加 1。
3、左右都是 1。此时 该位置会将两个旧段合并成一个新段。

实现时用到了link的想法 
"""


class Solution2:
    def findLatestStep(self, arr, m):
        link = [0] * (len(arr)+2)  # arr从1开始索引 同时头尾相当于哨兵节点 使link在跳转后能够恰当终止
        cnt, res = 0, -1  # cnt表示满足长度为m的数目

        # 情况2可以视为情况3的特例
        for i in range(len(arr)):
            x = arr[i]
            # 找到储存的左右端点的信息
            l = link[x-1] if link[x-1] else x
            r = link[x+1] if link[x+1] else x
            # 合并段
            if x-l == m:
                cnt -= 1  # 满足的数目数减1
            if r-x == m:
                cnt -= 1
            if r-l+1 == m:
                cnt += 1
            # 只要cnt>0就不断更新 那么最终返回的就是 **存在长度恰好为m的一组1的最后步骤**
            if cnt > 0:  # 如果还存在满足的情况，当前步更新
                res = i+1
            # 更新端点信息 将l/r替换为link列表中的位置就是题解中的更新式子
            link[l] = r
            link[r] = l

        return res


# s = Solution2()
# arr = [3, 5, 2, 4, 1]
# m = 1
# s.findLatestStep(arr, m)


class Solution3:
    def findLatestStep(self, arr, m):
        link = [0]*(len(arr)+2)
        count, step = 0, -1
        for i in range(len(arr)):
            pos = arr[i]
            left = link[pos-1] if link[pos-1] else pos
            right = link[pos+1] if link[pos+1] else pos

            if pos - left == m:
                # 情况1
                count -= 1
            if right - pos == m:
                # 情况2
                count -= 1
            
            if right - left + 1 == m:
                # 情况3
                count += 1
            
            if count > 0:
                step = i + 1

            link[left] = right
            link[right] = left
        return step

s = Solution3()
arr = [3, 1, 5, 4, 2]
m = 2
print(s.findLatestStep(arr, m))
