class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge_k_sorts(self, lists: list[ListNode]) -> ListNode:

        #Base case: if the list of lists is empty, return None
        if not lists:
            return None
        #Base case: if the list of lists has only one list, return that list
        if len(lists) == 1:
            return lists[0]
        
        #Iteratively merge pairs of lists until only one list remains
        while len(lists) > 1:
            merged_lists = []

            #Merge pairs of lists
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge_two_lists(list1, list2))
            
            #Update the list of lists with the merged lists
            lists = merged_lists
        #Return the final merged list
        return lists[0]
    
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #Create a dummy node to simplify the merging process
        dummy = ListNode()
        current = dummy

        #Merge the two lists by comparing their values
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        #If there are remaining nodes in either list, append them to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        #Return the merged list, which starts at dummy.next
        return dummy.next