🍬 Distribute Candies 🎉
👋 Welcome to the Distribute Candies project! This function helps determine the maximum number of different types of candies one can eat. Let’s jump right in! 🏊‍♂️

📚 Problem Statement
Given an integer array candyType of length n, where each integer represents a type of candy, you are to distribute the candies such that you maximize the number of different types of candies that you can eat. You are allowed to eat only n / 2 candies.

🛠️ Constraints
The length of the array n is even and ranges from [2, 10^4].

Each integer in the array candyType is in the range [-10^5, 10^5].

🌟 Example
Example 1
Input:

candyType = [1,1,2,2,3,3]
Output:

3
Explanation: You can eat 3 candies in total and there are 3 different types of candies.

Example 2
Input:

candyType = [1,1,2,3]
Output:

2
Explanation: You can eat 2 candies in total and there are 3 different types of candies.

🚀 How It Works
Calculate Unique Types:

Use a set to find the number of unique candy types.

Determine Maximum Types:

The maximum number of different types you can eat is either the total number of unique types or half the total number of candies, whichever is smaller.

---

### Approach
Use a set to count unique candy types, then return the minimum of that count and n // 2 (the allowed number of candies). This guarantees the maximum distinct types eaten under the constraint of taking only half of the candies.

### Complexity
- Time: O(n) to build the set of unique types
- Space: O(n) for the set