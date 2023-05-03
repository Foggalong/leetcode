class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a singly linked list, returns True if
        it is a palindrome or false otherwise. This one really
        highlighted that I don't know much about leveraging the
        structure of linked lists.
        """
        
        # convert linked list to a digit string
        current_value = [head.val]
        while head.next != None:
            current_value.append(head.next.val)
            head = head.next

        # compare to its reverse
        return current_value == current_value[::-1]
