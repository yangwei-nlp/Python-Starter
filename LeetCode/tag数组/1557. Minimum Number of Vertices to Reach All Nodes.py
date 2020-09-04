class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        froms = set([edge[0] for edge in edges])
        tos = set([edge[1] for edge in edges])
        
        return list(froms - tos)


s = Solution()
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]

print(s.findSmallestSetOfVertices(n, edges))
