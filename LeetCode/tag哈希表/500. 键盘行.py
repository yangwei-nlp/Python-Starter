class Solution:
    def findWords(self, words):
        char_line_tabel = {
            'q':1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 'o':1, 'p':1,
            'a':2, 's':2, 'd':2, 'f':2, 'g':2, 'h':2, 'j':2, 'k':2, 'l':2,
            'z':3, 'x':3, 'c':3, 'v':3, 'b':3, 'n':3, 'm':3
        }
        ret = []
        for word in words:
            first_char = word[0]
            if first_char not in char_line_tabel:
                line = 2
                if char_line_tabel[first_char.lower()] != line:
                    continue
            else:
                line = char_line_tabel[first_char]
            if word[1:]:
                for char in word[1:]:
                    if char not in char_line_tabel:
                        new_line = 2
                        if char_line_tabel[char.lower()] != new_line:
                            continue
                    else:
                        new_line = char_line_tabel[char]
                    if new_line != line:
                        break
                if new_line != line:
                    continue
                ret.append(word)
        return ret


s = Solution()
s.findWords(["Hello","Alaska","Dad","Peace"])