class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Step 1. Split the list to two halves
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None  # Break the list
        
        # Step 2. Recursively sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        # Step 3. Merge sorted l1 and l2
        return self.merge(l1, l2)
        
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
           
