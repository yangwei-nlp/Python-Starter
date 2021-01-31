class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result = "0"
        while len(result) < k:
            result = result + "1" + self.transform(result)
        return result[k-1]
    

    def transform(self, string):
        string = "0111001"
        anti_str = ''.join([str(1-int(string[i])) for i in range(len(string)-1, -1, -1)])
        return anti_str

n = 4
k = 11
# n = 3
# k = 1
s = Solution()
print(s.findKthBit(n, k))
