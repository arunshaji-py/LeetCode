
#define the list node class
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution():
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #create a dummy node to start with
        dummy = ListNode(-1)
        dummy.next = head

        #declare a pointer to the left of the group
        groupPrev = dummy

        while True:
            #find the Kth node
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            groupNext = kth.next
            #reverse the kth group
            prev = groupNext
            current = groupPrev.next

            while current != groupNext:
                temp = current.next 
                current.next = prev
                prev = current
                current = temp
                
            #update the pointers
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp


                
            


    