# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        first = ret
        while l1 != None or l2 != None:
            if l1 is None and l2 is not None:
                ret.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None and l1 is not None:
                ret.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val <= l1.val:
                ret.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None or l1.val <= l2.val:
                ret.next = ListNode(l1.val)
                l1 = l1.next
            ret = ret.next
        return first.next

def printa(first):
    ret = f'{first.val}'
    first = first.next
    while first != None:
        ret = ret + f'->{first.val}'
        first = first.next
    print(ret)
    return ret

def createList(lista):
    first = ListNode(lista[0])
    lista.pop(0)
    l = first
    for i in lista:
        l.next = ListNode(i)
        l = l.next
    return first

assert printa(Solution().mergeTwoLists(createList([1,2,4]), createList([1,3,4]))) == "1->1->2->3->4->4"
