class Solution:
    def nextGreatestLetter(self, letters: 'List[str]', target: 'str') -> 'str':
        if target < letters[0]:
            return letters[0]
        elif target >= letters[-1]:
            return letters[0]

        i = 0
        j = len(letters) - 1
        while j - i > 1:
            mid_index = (i + j) // 2
            if letters[mid_index] > target and letters[mid_index-1] <= target:
                return letters[mid_index]
            elif letters[mid_index] <= target and letters[mid_index-1] <= target:
                i = mid_index
            elif letters[mid_index] >= target and letters[mid_index-1] >= target:
                j = mid_index
        return letters[j]


s = Solution()
print(s.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"))