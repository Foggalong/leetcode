# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a sorted linked list, recusively deletes all duplicates  
        such that each element appears once. The returned list is sorted as well.
        """

        # if reached the end of the list, we're done
        if (head is None) or (head.next is None): return head

        # if subsequent values match, replace head with head.next after
        # its duplicates have been replaced
        if (head.val == head.next.val): return self.deleteDuplicates(head.next)
    
        # otherwise, remove duplicates from head.next
        return ListNode(head.val, self.deleteDuplicates(head.next))

