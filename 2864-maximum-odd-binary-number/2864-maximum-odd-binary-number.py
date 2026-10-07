class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        r = ""
        for i in range(0,len(s)):
            if(s[i] == "1"):
                count += 1
        for i in range(0,count -1):
            r  = r + "1"
        for i in range(0,len(s)-count):
            r = r + "0"
        r = r + "1"
        return r
