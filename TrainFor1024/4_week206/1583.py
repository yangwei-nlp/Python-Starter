# 脑筋急转弯 u就像是个第三者，x和u互相更喜欢，而不那么喜欢自己原配
class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        friend_pair = {}
        for pair in pairs:
            friend_pair[pair[0]] = pair[1]
            friend_pair[pair[1]] = pair[0]

        ans = 0
        for x in range(n):
            cp_idx = preferences[x].index(friend_pair[x])
            for u in preferences[x][:cp_idx]:
                v = friend_pair[u]
                u_prefs = preferences[u]
                if u_prefs.index(x) < u_prefs.index(v):
                    ans += 1
                    break
        return ans


n = 4
preferences = [[1,3,2],[2,3,0],[1,3,0],[0,2,1]]
pairs = [[1,3],[0,2]]

s = Solution()
print(s.unhappyFriends(n, preferences, pairs))

