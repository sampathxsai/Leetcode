class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = -1
        x = 0
        flag = 0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if(s[i]== s[j]):
                    x = j-i-1
                    if(x>m):
                        m = x
        return m