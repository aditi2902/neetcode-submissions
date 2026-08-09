# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        dummy=head
        carry=0## important
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            z=x+y+carry
            carry=z//10
            value=z%10
            dummy.next=ListNode(value)
            dummy=dummy.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
        return head.next