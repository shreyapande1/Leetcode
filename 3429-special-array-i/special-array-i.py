class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(sum(p)%2 for p in pairwise(nums))  