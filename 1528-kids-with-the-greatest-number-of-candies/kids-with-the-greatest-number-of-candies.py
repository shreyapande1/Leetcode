class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        mc = max(candies)
        for i in range (len(candies)):
            if candies[i] + extraCandies >= mc:
                candies[i] = True
            else:
                candies[i] = False
        return candies
        