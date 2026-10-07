class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        x = prices[0]+prices[1]
        if(x>money):
            return money
        else :
            return money - x