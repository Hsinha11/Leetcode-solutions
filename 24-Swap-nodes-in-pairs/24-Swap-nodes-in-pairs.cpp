#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head -> next == NULL){
            return head;
        }
            
        ListNode* temp = head->next;
        
        head->next = swapPairs(head->next->next);
        temp->next = head;
        
        return temp;
    }
};