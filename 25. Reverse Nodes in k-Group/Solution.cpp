/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
// Approach: For each segment, find the k-th node. If fewer than k remain, stop.
// Otherwise detach [ptr..kth], reverse it, and stitch it back between the
// previous tail and the next segment's head. Repeat until done.
// Time: O(n), Space: O(1) auxiliary (recursive reverse uses call stack).
class Solution {
public:
    ListNode* reverseLL(ListNode* head)
    {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode *new_head = reverseLL(head->next);
        ListNode *front = head->next;
        front->next = head;
        head->next = NULL;
        return new_head;
    }
    ListNode* findKthNode(ListNode* temp, int k)
    {
        for(int i = 1; i<k;i++)
        {
            temp = temp->next;
            if(temp == NULL)
                return NULL;
        }
        return temp;
    }
    ListNode* reverseKGroup(ListNode* head, int k) 
    {
        ListNode* ptr = head;
        ListNode* prevnode = NULL;
        while(ptr)
        {
            ListNode* kthnode = findKthNode(ptr,k);
            if(kthnode == NULL)
            {
                if(prevnode)
                    prevnode->next = ptr;
                break;
            }
            ListNode* ahead = kthnode->next;
            kthnode->next = NULL;
            ListNode* newhead = reverseLL(ptr);
            if(ptr == head)
            {
                head = newhead;
            }
            else
            {
                prevnode->next = newhead;
            }
            prevnode = ptr;
            ptr = ahead;
        }
        return head;
    }
};
