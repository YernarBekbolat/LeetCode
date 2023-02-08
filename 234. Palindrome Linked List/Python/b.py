# O(n) complexity solution with classis LL code.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(self, head):
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node

    return prev_node

def isPalindrome(self, head):
    fast = slow = head

    while fast.next != None and fast != None:
        fast = fast.next.next
        slow = slow.next

    fast = head
    slow = self.reverse(slow)

    while slow != None:
        if slow.val != fast.val:
            return False

        fast = fast.next
        slow = slow.next

    return True