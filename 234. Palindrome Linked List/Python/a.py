class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head):
    s = ""
    while (head != None):
        s += str(head.val)
        head = head.next

    return s == s[::-1]