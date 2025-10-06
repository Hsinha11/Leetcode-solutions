#include <string>
using namespace std;

class Solution {
public:
    string largestOddNumber(string num) {
        // Start from the rightmost digit and find the first odd digit
        for (int i = num.length() - 1; i >= 0; i--) {
            // If current digit is odd
            if ((num[i] - '0') % 2 == 1) {
                // Return the substring from start to this odd digit
                return num.substr(0, i + 1);
            }
        }
        // If no odd digit found, return empty string
        return "";
    }
};