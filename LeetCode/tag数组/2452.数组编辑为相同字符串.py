from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        LEN = len(queries[0])
        def change_able(word1, word2):
            change_cnt = 0
            for i in range(LEN):
                if word1[i] != word2[i]:
                    change_cnt += 1
            return change_cnt <= 2

        res = []

        for q in queries:
            for d in dictionary:
                if change_able(q, d):
                    res.append(q)
                    break
        return res