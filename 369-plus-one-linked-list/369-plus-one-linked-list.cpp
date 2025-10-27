// LeetCode 369. Plus One Linked List
// Approach: Reverse the list, add one with carry, and reverse again
// Time Complexity: O(n), Space Complexity: O(1)

#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) {
            ListNode* nxt = head->next;
            head->next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }

    ListNode* plusOne(ListNode* head) {
        head = reverse(head);
        ListNode* curr = head;
        int carry = 1;

        while (curr && carry) {
            curr->val += carry;
            carry = curr->val / 10;
            curr->val %= 10;
            if (!curr->next && carry)
                curr->next = new ListNode(0);
            curr = curr->next;
        }

        return reverse(head);
    }
};
