# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        if temp == None or temp.next == None:
            return None
        while temp != None:
            count = count + 1
            temp = temp.next
        n = count - n + 1
        i = 1
        temp = head
        prev = None
        if n == 1:
            head = head.next
            return head
        while temp != None and i < n:
            prev = temp
            temp = temp.next
            i = i + 1
        temp = temp.next
        if temp == None:
            prev.next = None
        else:
            prev.next = temp
        return head
