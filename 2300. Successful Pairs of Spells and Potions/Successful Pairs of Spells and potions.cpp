class Solution {
    public:
        vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
            // Sort the potions array so we can use binary search efficiently
            sort(potions.begin(), potions.end());
            int m = potions.size();  // Number of potions
            vector<int> result;      // To store the count of successful pairs for each spell
    
            // Iterate through each spell
            for (long long spell : spells) {
                // To achieve at least 'success', potion must satisfy:
                // spell * potion >= success
                // => potion >= success / spell
                // We use ceiling division to avoid floating-point errors:
                // required = ceil(success / spell)
                long long required = (success + spell - 1) / spell;
    
                // Use binary search to find the first potion >= required
                // lower_bound returns the iterator pointing to the first element
                // not less than 'required'
                int idx = lower_bound(potions.begin(), potions.end(), required) - potions.begin();
    
                // All potions from idx to end of array form successful pairs with this spell
                result.push_back(m - idx);
            }
    
            // Return the result vector containing successful pair counts for each spell
            return result;
        }
    };
    