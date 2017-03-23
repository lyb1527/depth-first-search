'''
Given a collection of numbers C and a target number T, find all the
unique combinations in C where the candidates sum to T

Each value can only be used ONCE:


Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]

'''

class Solution():
    '''
    @param candidates: given the candidate numbers
    @param target: the target
    @treturn: all the combinations that sum to target
    '''

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.ans = []
        tmp = []
        use = [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, tmp, use)
        return self.ans

    def dfs(self, can, target, p, now, tmp, use):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p, len(can)):
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):
                tmp.append(can[i])
                use[i] = 1
                self.dfs(can, target, i+1, now + can[i], tmp, use)
                tmp.pop()
                use[i] = 0

s = Solution()
a = [1, 2, 3, 4, 5]
print(s.combinationSum2(a, 10))
