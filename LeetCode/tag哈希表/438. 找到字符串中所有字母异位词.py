from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s) < len(p): return []
        window = len(p)
        ret = []
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(window):
            d1[s[i]] += 1
        for i in range(window):
            d2[p[i]] += 1
        if self.check(d1, d2):
            ret.append(0)
        for i in range(window, len(s)):
            d1[s[i]] += 1
            d1[s[i - window]] -= 1
            if self.check(d1, d2):
                ret.append(i - window + 1)
        return ret

    def check(self, d1, d2):
        for char, cnt in d2.items():
            if cnt != d1[char]:
                return False
        return True