#Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

def maxProfit(prices):
        left,right=0,1
        maxProfit=0
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxProfit=max(maxProfit,profit)
            else:
                left=right
            right+=1
        return maxProfit

'''
Approach (Two Pointers - Sliding Window):
1.Goal:
You want to maximize your profit by buying low and selling high, but the buy must happen before the sell.

2.Initialize Two Pointers:
left starts at index 0 — this represents the buy day.
right starts at index 1 — this represents the sell day.

3.Iterate Through the Array:
Move the right pointer one step at a time.
At each step, compare the prices at left and right.

4.Check for Profit Opportunity:
If prices[right] > prices[left]:
You can make a profit by buying at left and selling at right.
Calculate profit = prices[right] - prices[left].
Update maxProfit if this profit is higher than the current maximum.
Else:
If prices[right] <= prices[left], it means the current right is a better candidate for a new minimum buy price, so move left = right.

5.Continue Until End of Array:
Keep moving right until it reaches the end of the list.

6.Return maxProfit:
This will be the highest profit found during the traversal.
If no profit was possible, it will return 0.
'''