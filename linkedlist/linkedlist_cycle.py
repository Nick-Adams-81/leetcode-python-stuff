# Defining the list node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def has_cycle(self, head: list[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

list = [1,2,3,4]
print(has_cycle(list))
