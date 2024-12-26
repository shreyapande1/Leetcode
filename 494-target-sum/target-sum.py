class Solution:
    def __init__(self):
        self.dp = []
        self.OFFSET = 1000 

    def solve(self, ind, nums, target):
      
        if ind >= len(nums):
            return 1 if target == 0 else 0

       
        if self.dp[ind][target + self.OFFSET] != -1:
            return self.dp[ind][target + self.OFFSET]

        
        ans = 0
        ans += self.solve(ind + 1, nums, target - nums[ind])  
        ans += self.solve(ind + 1, nums, target + nums[ind])  

      
        self.dp[ind][target + self.OFFSET] = ans
        return ans

    def findTargetSumWays(self, nums, target):
        
        self.dp = [[-1] * 3002 for _ in range(len(nums))]
        return self.solve(0, nums, target) 