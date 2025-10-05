#include <string>
using namespace std;

class Solution {
public:
    string largestGoodInteger(string num) {
        char maxDigit = '\0';  // Initialize with null character
        
        // Check each possible substring of length 3
        for (int i = 0; i <= num.length() - 3; i++) {
            // If three consecutive digits are same
            if (num[i] == num[i + 1] && num[i + 1] == num[i + 2]) {
                // Update maxDigit if current digit is larger
                maxDigit = max(maxDigit, num[i]);
            }
        }
        
        // If we found a valid digit, return string with three occurrences of it
        if (maxDigit != '\0') {
            return string(3, maxDigit);
        }
        
        // If no valid substring found, return empty string
        return "";
    }
};