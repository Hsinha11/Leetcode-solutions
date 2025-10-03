/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// Approach: Copy value from next node into current, then bypass next node by
// setting current->next = current->next->next. This removes the next node,
// which is equivalent to deleting the given node when head isn't available.
// Time: O(1), Space: O(1)
class Solution {
    
public:
Solution(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
    }
    void deleteNode(ListNode* node) {
        node->val= node->next->val;node->next = node->next->next;
    }
};