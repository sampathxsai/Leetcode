class Solution:
    def maxScore(self, s: str) -> int:
        tot = 0
        for i in range(0,len(s)):
            tot += int(s[i])
        max = 0
        z = 0
        x = 0
        for i in range(0,len(s)-1):
            if(int(s[i]) == 0):
                z += 1
            else:
                x += 1
            if z+(tot-x) > max:
                max = z+(tot-x)
        return max