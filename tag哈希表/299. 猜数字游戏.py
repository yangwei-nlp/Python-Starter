class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 思路：首先得到共有多少个重复的（total），再计算A，
        # B=total-A
        # 复杂度为O(3N)
        num_cnt = {}
        for char in secret:
            if char not in num_cnt:
                num_cnt[char] = 1
            else:
                num_cnt[char] += 1
        total = 0
        for char in guess:
            if char in num_cnt:
                if num_cnt[char] >= 1:
                    num_cnt[char] -= 1
                    total += 1
        result_A = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                result_A += 1
        return "{}A{}B".format(result_A, total-result_A)