class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0,len(s)):
            flag = 0
            for j in range(0, len(s)):
                if(i==j):
                    continue
                elif(s[i]==s[j]):
                    flag = 1
                    break
            if(flag==0):
                return i
        return -1