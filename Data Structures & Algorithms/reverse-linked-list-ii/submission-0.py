class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head is None or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node before left
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # curr is the first node we need to reverse
        curr = prev.next

        # Reverse left -> right
        for _ in range(right - left):
            nxt = curr.next

            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next