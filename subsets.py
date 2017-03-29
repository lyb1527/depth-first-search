'''
Given a set of distinct integers, return all possible subsets.
    *Elements in a subset must be in non-descending order.
    *The solution set must not contain duplicate subsets.

If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
class Solution:

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
