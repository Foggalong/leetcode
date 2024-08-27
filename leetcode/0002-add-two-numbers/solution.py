# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # initialise variables 
        value = l1.val + l2.val
        digits = []

        # process all common digit positions
        while True:
            carry = 0  # reset carry
            # if sum is two digits, save last digit and carry the 1
            if value > 9:
                value -= 10
                carry += 1
            # add new value to output
            digits.append(value)

            # case where both ListNodes are done
            if l1.next is None and l2.next is None:
                break

            # start computing next value
            value = carry
            if l1.next is not None:
                l1 = l1.next
                value += l1.val
            if l2.next is not None:
                l2 = l2.next
                value += l2.val

        # add final carry
        if carry > 0:
            digits.append(carry)

        # reformat digit list as a ListNode
        output = ListNode(digits[-1], None) 
        for digit in digits[-2::-1]:
            output = ListNode(digit, output)

        return output
