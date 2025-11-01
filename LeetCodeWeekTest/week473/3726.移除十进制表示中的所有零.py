class Solution:
    def removeZeros(self, n: int) -> int:
        n_str = str(n)

        ret = ""
        for chr in n_str:
            if chr != "0":
                ret += chr
        return int(ret)