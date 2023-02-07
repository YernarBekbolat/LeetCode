class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(self, node):
    # Deleted node gets value of next node
    node.val = node.next.val 
    # Deleting node
    node.next = node.next.next