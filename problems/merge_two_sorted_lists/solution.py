class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Takes two linked lists as input (both optional) and
        merges the two into one sorted list, which is returned.
        """

        # cover cases where either/both list not provided
        if list1 is None: return list2
        if list2 is None: return list1

        # build a stack of ascending entries
        stack = []

        # ¬(A ^ B) quicker to check than (¬A v ¬B) 
        while not (list1 is None and list2 is None):
            # if list1 empty, add all remaining list2 values
            if list1 is None:
                while list2 is not None:
                    stack.append(list2.val)
                    list2 = list2.next
            # if list2 empty, add all remaining list1 values
            elif list2 is None:
                while list1 is not None:
                    stack.append(list1.val)
                    list1 = list1.next
            # add smallest head and advance that list
            elif (list1.val < list2.val):
                stack.append(list1.val)
                list1 = list1.next
            else:
                stack.append(list2.val)
                list2 = list2.next

        # pop items off stack into ascending linked list
        output = None
        while stack:
            output = ListNode(stack[-1], output)
            stack.pop(-1)

        return output
