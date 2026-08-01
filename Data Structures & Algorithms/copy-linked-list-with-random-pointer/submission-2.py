"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None 
        
        temp = head
        head1 = Node(temp.val)
        temp1 = head1
        node_map = {}
        node_map[temp] = temp1
        temp = temp.next
        while temp != None:
            temp1.next = Node(temp.val)
            node_map[temp] = temp1.next
            temp = temp.next
            temp1 = temp1.next
            temp1.random = None
            
        temp = head
        temp1 = head1
        while temp != None:
            if temp.random != None:
                temp1.random = node_map[temp.random]
            else:
                temp1.random = None
            temp = temp.next
            temp1 = temp1.next
            
        return head1
