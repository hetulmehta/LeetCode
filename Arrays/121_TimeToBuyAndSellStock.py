class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """O(N^2) Solution
        profit=[]
        for i in range(len(prices)-1):
            if max(prices[i+1:])>prices[i]:
                profit.append(max(prices[i+1:])-prices[i])
        if profit:
            return max(profit)
        else:
            return 0
        """
        # O(N) optimal solution keeps track of seeling date and keeps tab of profit with the min value before it.
        #[2,4,1]
        #[0,1,2] profit when 2 is the sell date:0; 4:2, 1:-1
        min=prices[0]
        profit=[]
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            profit.append(prices[i]-min)
        return max(profit)
    