class Solution:
    def longestPalindrome(self, s: str) -> str:
        text='*'+'*'.join(s)+'*'
        n=len(text)
        j=0
        for i in range(n-1):
            mirror=2*i-j
            while mirror>=0 and j<n and text[i+1:j+1]==text[mirror:i][::-1]:
                result=text[mirror+1:j+1:2]
                j+=1
                mirror=2*i-j
            j=i+1+(j-i)
            if j>=n:
                break
        return result
        