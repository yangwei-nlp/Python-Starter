class Solution:
    def isTransformable(self, s, t):
        if not s:
            return True
        
        i = 0
        back_idx = len(s)-1
        while i < back_idx:
            # print(s[i])
            this_char = s[i]
            next_char = s[i+1]

            if -1 in [t.find(s[i]), t.find(s[i+1])]:
                return False
            else:
                t_this_char_idx = t.find(s[i])
                t_next_char_idx = t.find(s[i+1])

            # 交换或False
            if t_this_char_idx > t_next_char_idx:
                if this_char > next_char:
                    # 交换
                    s_list = list(s)
                    s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                    s = "".join(s_list)
                else:
                    return False
            i += 1
        s, t = self.cut_string(s, t)
        return self.isTransformable(s, t)


    def cut_string(self, s, t):
        front_idx = 0
        for i in range(len(s)):
            if s[i] == t[i]:
                front_idx = i
            else:
                break
        
        back_idx = -1
        for j in range(len(s)-1, -1, -1):
            if s[j] == t[j]:
                back_idx = j
            else:
                break
        if back_idx == -1:
            return s[front_idx: ], t[front_idx: ]
        else:
            return s[front_idx: back_idx], t[front_idx: back_idx]


s = "1"
t = "2"

ss = Solution()
print(ss.isTransformable(s, t))

# print(ss.cut_string(s, t))

