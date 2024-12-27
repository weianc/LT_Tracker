# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = head
        while fast is not None: 
            if slow.val != fast.val: 
                slow.next = fast
                slow = slow.next
            
            fast = fast.next

        # at the end of the traverse 
        # should assign slow to none to end the duplicate node 
        slow.next = None

        return dummy.next