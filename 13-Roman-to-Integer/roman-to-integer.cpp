// LeetCode 13: Roman to Integer
// ------------------------------------------------------------
// Problem: Convert a Roman numeral string into its integer value.
// Approach: Traverse the string, adding or subtracting based on
//           the relative value of consecutive Roman symbols.
// ------------------------------------------------------------
// Time Complexity: O(n)  → one pass through the string
// Space Complexity: O(1) → constant map of 7 symbols
// ------------------------------------------------------------

#include <unordered_map>
#include <string>
using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        // Step 1: Mapping Roman numerals to their integer values
        unordered_map<char, int> roman = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};

        int result = 0; // Variable to store the final integer value

        // Step 2: Iterate through each character in the string
        for (int i = 0; i < s.size(); ++i)
        {
            int curr = roman[s[i]];                              // Current numeral value
            int next = (i + 1 < s.size()) ? roman[s[i + 1]] : 0; // Next numeral value (if any)

            // Step 3: Apply subtraction rule
            // If the current numeral is smaller than the next one, subtract it.
            // Otherwise, add it to the result.
            if (curr < next)
            {
                result -= curr;
            }
            else
            {
                result += curr;
            }
        }

        // Step 4: Return the computed integer value
        return result;
    }
};

