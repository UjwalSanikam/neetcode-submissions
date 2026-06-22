# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1 = head
        list2 = slow.next
        slow.next = None
        curr = list2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        list2 = prev
        head = list1
        temp = head
        list1 = list1.next
        count = 0
        while list1 and list2:
            if count % 2 == 0:
                temp.next = list2
                count = count + 1
                list2 = list2.next
            else:
                temp.next = list1
                count = count + 1
                list1 = list1.next
            temp = temp.next
        if list2 == None:
            temp.next = list1
        else:
            temp.next = list2
        