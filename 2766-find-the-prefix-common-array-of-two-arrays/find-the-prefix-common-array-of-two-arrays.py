class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        x, y = set(), set()
        ans = []

        for i in range(n):
            a, b = A[i], B[i]
            x.add(a)
            y.add(b)
            ans.append(len(x & y))  # Intersection of x and y
        
        return ans