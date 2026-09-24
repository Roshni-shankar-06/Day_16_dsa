class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1. Split the list to two halves
        prev, slow, fast = None, head, head
        while fast and fast.next:
          
