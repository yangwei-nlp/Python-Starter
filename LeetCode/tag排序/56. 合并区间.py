# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = [[x.start, x.end] for x in intervals]
        intervals.sort(key=lambda x: (x[0], x[1]))

        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                del intervals[i]  # 这个删除很巧妙，因为没有将i加1所以不会出错
            else:
                i += 1

        return intervals