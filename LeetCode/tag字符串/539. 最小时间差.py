# 我的原始思路：
"""
将原始字符串时间排序，随后按照顺序依次计算两个时间的分钟差值，然后一直比较到最后一个时间,
最后返回最小的那个时间
"""


# 下面思路源于网络
"""
第一个trick: 意识到所有分钟制时间都是24*60分钟中的一个,所以第一可以通过一个萝卜一个坑的思想，
也就是说，我可以将所有时间转化为分钟，如果后续发现有时间和之前的时间有重复，说明最短间隔就是0

另外，其他的思想差不多，也是通过排序找到最小的间隔
"""
class Solution:
    def findMinDifference(self, timePoints):
        hasTime = [False] * (24*60)  # 一个萝卜(时间)一个坑
        times = []
        for time_str in timePoints:
            all_minute = self.time2minute(time_str)
            if hasTime[all_minute]:
                return 0
            else:
                hasTime[all_minute] = True
                times.append(all_minute)
        times.sort()
        
        min_gap = 1e10
        for i in range(len(timePoints)-1):
            tmp_gap = times[i+1] - times[i]
            if tmp_gap < min_gap:
                min_gap = tmp_gap
        """
        下面这句程序处理这种情况：
        00:10和23:50，如果计算从00:00到00:11,00:12,...,23:49,23:50，数字则会很大，
        但是反过来计算从23:51到23:52,...,00:09，gap则会很小
        因为时间是个圈，所以必须对首尾进行特殊处理，如下程序：
        """
        min_gap = min(min_gap, 1440-times[-1]+times[0])
        return min_gap


    def time2minute(self, time):
        # result 表示从0到time需要多少分钟
        result = 0
        hour, minute = time.split(':')
        result += int(hour) * 60
        result += int(minute)
        return result


s = Solution()
print(s.findMinDifference(['20:46', '15:29']))
