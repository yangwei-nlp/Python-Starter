# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n = len(intervals)
        start_map = {interval.start : i for i, interval in enumerate(intervals)}
        start_list = [interval.start for interval in intervals]
        res = []
        start_list.sort()
        for interval in intervals:
            pos = self.higher_find(start_list, interval.end)
            res.append(start_map[start_list[pos]] if pos != -1 else -1)
        return res

    def higher_find(self, array, v):
        lo, hi = 0, len(array) - 1
        first = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if array[mid] >= v:
                hi = mid - 1
                first = mid
            else:
                lo = mid + 1
        return first

s = Solution()
print(s.findRightInterval([Interval(3,4), Interval(2,3), Interval(1,2)]))
