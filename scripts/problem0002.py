#!/anaconda3/envs/py37/bin/python

#https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = ListNode(0)
        head = n
        carry = 0
        while l1 or l2:
            val = 0
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next
            val = val + carry
            carry, num = divmod(val, 10)
            n.next = ListNode(num)
            n = n.next

        if carry > 0:
            n.next = ListNode(num)
            #n = n.next

        return head.next

    def printList(self, l : ListNode):
        while l:
            print(l.val, end='')
            l = l.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
ans = s.addTwoNumbers(l1, l2)
s.printList(ans)

