from typing import Optional

class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        #grab the each digits from the linked list
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
        
            #do the core addition

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10


             #append result digit and advance.
            current.next = ListNode(digit)
            current = current.next

             #advance each list pointer if not exhausted
            if l1:l1 = l1.next
            if l2: l2 = l2.next
 
        return dummy.next

