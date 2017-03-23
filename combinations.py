'''
Given two intergers, n and k, return all possible combination of k numbers
out of 1 to n

EXAMPLE:

For example,
If n = 4 and k = 2, a solution is:
[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

Tags
'''

class Solution:
    '''
    # param: n given the range of numbers
    # param: k given the number of in each of the combinations
    # return : all combinations of k numbers of 1 ...n
    '''
    def combine(self, n, k):
        self.result = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.result


    def dfs(self, n, k, m, p, tmp):
        if k == p:
            self.result.append(tmp[:])
            return
        for i in range(m, n+1):
            tmp.append[i]
            self.dfs(n, k, i+1, p+1, tmp)
            tmp.pop()

s = Solution()
print(s.combine(4, 2))
