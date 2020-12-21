class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        even = len(palindrome) % 2 == 0
        if even:
            stop = len(palindrome) // 2 + 1
        else:
            stop = len(palindrome) // 2
        for i, char in enumerate(palindrome[:stop]):
            if char > 'a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'


s = Solution()
print(s.breakPalindrome('aaaa'))
