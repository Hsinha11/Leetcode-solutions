Best Time to Buy and Sell Stock 📈

👋 Welcome to the Best Time to Buy and Sell Stock project! This function helps you find the maximum profit you can make from a single buy and sell operation in a series of stock prices. Simple, efficient, and very practical! Let’s dive in. 🏊‍♀️

📚 Problem Statement:

You are given an array prices where prices[i] represents the price of a stock on day i.

Your task is to maximize your profit by choosing one day to buy and one day to sell the stock. You must buy before you sell.

If no profit is possible, return 0.

🛠️ Constraints:

The length of prices is in the range [1, 10^5].

Each price is in the range [0, 10^4].

🌟 Example:

Example 1
Input:

prices = [7,1,5,3,6,4]


Output:

5


Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6). Profit = 6 - 1 = 5.

Example 2
Input:

prices = [7,6,4,3,1]


Output:

0


Explanation: No transaction is done, so the max profit = 0.

🚀 How It Works

Initialization:

1.Keep track of the minimum price seen so far (min_price).

2.Keep track of the maximum profit (max_profit).

Iteration:

1.For each price in the list:

    a.Update the min_price if the current price is lower.

    b.Calculate the profit if we sell at the current price.

    c.Update max_profit if this profit is higher than before.

    d.Return Result:

Return the max_profit at the end.
This approach runs in O(n) time and O(1) space — perfect for large input sizes! ⚡