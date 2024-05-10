class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, returns the middle node
        of the linked list. If there are two middle nodes, it returns
        the second middle node.
        """

        middle     = head  # guaranteed at least one node 
        even_index = True  # first node checked will be #2 (even)

        while head.next != None:
            # move linked list forward
            head = head.next
            # every other node, move the middle forward
            if even_index:
                middle = middle.next
            # flip even/odd tracker
            even_index = not even_index
        
        return middle




