

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    '''
    Reverse singly linked list

    :type head: ListNode
    :rtype: ListNode
    '''

    stack = []
    current = head
    while current:
        stack.append(current)
        current = current.next

    if stack:
        new_head = stack[-1]
    else:
        new_head = None

    for node in reversed(stack):

        stack.pop()

        if stack:
            node.next = stack[-1]
        else:
            node.next = None

    return new_head
