# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        curr=head
        prev=None
        count =1
        while temp.next is not None:
            count+=1
            temp=temp.next
            
        m=count-n
        if m==0:
            head=head.next
            return head
        else:
            i=0
            while i<m:
                prev=curr
                curr=curr.next
                i+=1
            prev.next=curr.next
            curr.next=None
        return head
        