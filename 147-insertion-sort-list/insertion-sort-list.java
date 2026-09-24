class Solution {
  public ListNode insertionSortList(ListNode head) {
    ListNode dummy = new ListNode(0);
    ListNode prev = dummy; // the last and thus largest of the sorted list

    while (head != null) {       // the current inserting node
      ListNode next = head.next; // Cache the next inserting node.
      if (prev.val >= head.val)
