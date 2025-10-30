# 24. Swap Nodes In Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example
Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]


Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

## Constraints

The number of nodes in the list is in the range [0, 100].

0 <= Node.val <= 100

## Approach

1. **Base Case:**  
   - If the list is empty (`head == None`) or has only one node, return it directly.
2. **Swap Logic:**  
   - Let `temp = head.next` (second node in the pair).  
   - Recurse on `head.next.next` to swap the remaining list.  
   - Rearrange pointers:
     - `head.next = swapPairs(head.next.next)`
     - `temp.next = head`
3. **Return `temp`** as the new head of the swapped pair.