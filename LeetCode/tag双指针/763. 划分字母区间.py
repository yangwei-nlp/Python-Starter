class Solution:
    def partitionLabels(self, S: 'str') -> 'List[int]':
        farthest = {}
        # 用来存储每个字母的最远索引
        for i in range(len(S)):
            farthest[S[i]] = i

        result = []
        i = 0
        j = farthest[S[i]]
        if j == len(S) - 1:
            return [len(S)]
        while j != len(S) - 1:
            j = farthest[S[i]]
            start = i
            while i != j:
                if j >= farthest[S[i]]:
                    i += 1
                else:
                    j = farthest[S[i]]
                    i += 1
            result.append(j-start+1)
            i += 1
        return result