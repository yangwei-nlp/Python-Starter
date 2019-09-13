class Solution:
    def getRow(self, rowIndex):
        last_row = [1]
        if rowIndex == 0:
            return last_row
        while rowIndex > 0:
            last_row.insert(0, 0)
            last_row.append(0)
            temp_row = list(map(lambda pair: pair[0] + pair[1], zip(last_row[:-1], last_row[1:])))
            last_row = temp_row
            rowIndex -= 1
        return temp_row


s = Solution()
print(s.getRow(3))