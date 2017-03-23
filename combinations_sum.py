'''
Given a set of candidates number C and a target number T, find all unique
combinations in C where the candidate numbers sum to T

NOTE: the same repeated number may be chosen from C unlimited number of time

EXAMPLE:
Given candidate set [2,3,6,7] and target 7, a solution set is:
[7]
[2, 2, 3]
'''
class Solution:
    # @param candidates, a list of intergers
    # @parame target, an interger
    # @return: list of list of intergers
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        candidates.sort()
        Solution.ret = []
        self.dfs(candidates, target, 0, [])
        return Solution.ret

    def dfs(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i, valuelist + [candidates[i]])


s = Solution()
alist = [1, 2, 3, 4, 5]
print(s.combinationSum(alist, 10))
