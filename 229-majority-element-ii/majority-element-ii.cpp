class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
            // comments are added in this solution to explain how this approach works and the intuition behind it 
            // we can optimise the solution to this problem by extending the existing  Boyer-Moore Voting Algorithm
            int n = nums.size();
            vector<int> result;
            // There can be at most two majority elements (appearing more than n/3 times)
            // to solve this declare the potential canditates as c1,c2 these canditates can appear as majority and their counts as cnt1,cnt2 denote how many times they appear
            int c1 = 0, c2 = 0;
            int cnt1 = 0, cnt2 = 0;
            // we solve the problems in two phases
            // phase 1 : determine the majority elements
            for (int num : nums) {
                // normally count the counts of element if the element
                if (num == c1) {
                    cnt1++;
                } else if (num == c2) {
                    cnt2++;
                }
                // it means that the current element is not really the majority,we refactor the new majority elements by selecting the new element and reset the counts
                else if (cnt1 == 0) {
                    c1 = num;
                    cnt1 = 1;
                } 
                else if (cnt2 == 0) {
                    c2 = num;
                    cnt2 = 1;
                } 
                //meaning that current element is not equal to the selected candidate since it isnt majority we decrement the counts 
                else {
                    cnt1--;
                    cnt2--;
                }
            }
            // phase 2 : Verify that the selected candidates indeed appear more than ⌊n/3⌋ times
            //reset counts to verify if these elements are indeed majority
            // here we are simply counting the occurences of the canditates we got in phase1
            cnt1 = 0;
            cnt2 = 0;
            for (int num : nums) {
                if (num == c1) {
                    cnt1++;
                } else if (num == c2) {
                    cnt2++;
                }
            }
            // now simply verify and push back the results
            if (cnt1 > n / 3) {
                result.push_back(c1);
            }
            if (cnt2 > n / 3) {
                result.push_back(c2);
            }
            // return the result which contains majority elements 
            return result;
    }
    // the proposed solution uses modification of Boyer-Moore Voting Algorithm and solves the given problem in linear time complexity O(n) and no extra space i.e space complexity -> O(1). 
};