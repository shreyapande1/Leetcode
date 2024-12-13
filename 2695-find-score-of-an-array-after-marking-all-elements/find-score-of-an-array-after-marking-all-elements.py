class Solution:
    def findScore(self, nums: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(nums)):
            if not stk or nums[i] < stk[-1]:
                stk.append(nums[i])
            else:
                while stk:
                    res += stk.pop()
                    if stk:
                        stk.pop()
        while stk:
            res += stk.pop()
            if stk:
                stk.pop()

        return res