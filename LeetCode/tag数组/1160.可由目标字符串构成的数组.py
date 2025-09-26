from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def char_cnt(word):
            res = {}
            for c in word:
                if c in res:
                    res[c] += 1
                else:
                    res[c] = 1
            return res

        def include(cnt1, cnt2):
            for k, v in cnt1.items():
                if k not in cnt2 or v > cnt2[k]:
                    return False
            return True

        res = 0
        tgt_cnt = char_cnt(chars)
        for word in words:
            cnt1 = char_cnt(word)
            if include(cnt1, tgt_cnt):
                res += len(word)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(["cat","bt","hat","tree"], "atach"))