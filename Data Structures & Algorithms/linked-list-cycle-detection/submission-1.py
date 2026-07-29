# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        trav=set()
        temp=head
        flag=False
        while temp:
            if temp.next in trav:
                flag=True
                return flag
            trav.add(temp)
            temp=temp.next
        return flag

    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next

            if fast==slow:
                return True
        return False
        
        
        
        
        """
