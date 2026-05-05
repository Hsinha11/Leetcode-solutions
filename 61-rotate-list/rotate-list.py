# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ListNode * prev =NULL, *curr = NULL;
#         for ( int i =0 ;i < k ;i ++){
#             curr = head;
#             prev = curr;
#             while ( curr!=NULL){
#                 prev=curr;
#                 curr=curr->next;           
#             }
#             // curr->next=head;
#             // prev->next=NULL;
#             // head=curr;
#         }
#         return head;
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        
        n=0
        temp =head
        while(temp):
            n+=1
            temp=temp.next
        
        k=k%n
        prev =None
        curr = None
        
        for i in range(k):
            curr = head
            prev = curr
            while ( curr.next!=None):
                prev=curr
                curr=curr.next
                
            
            
            curr.next=head
            head=curr
            prev.next=None
        
        
        return head
        