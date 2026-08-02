# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow=head
        fast=head.next
        while fast and fast.next: ## if fast at end means slow at middle
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        prev=slow.next=None ##split into 2 halves
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        f,s=head,prev ##merge the havles
        while s:
            tmp1,tmp2=f.next,s.next 
            f.next=s
            s.next=tmp1 
            f,s=tmp1,tmp2 
        

        