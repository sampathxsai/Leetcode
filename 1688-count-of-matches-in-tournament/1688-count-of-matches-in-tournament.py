class Solution:
    def numberOfMatches(self, n: int) -> int:
        mat = 0 
        y = n
        while(y>1):
            if(y%2==0):
                mat = mat + y//2
                y  = y//2
            else:
                mat = mat + (y-1)//2
                y = (y-1)//2 + 1
        return mat