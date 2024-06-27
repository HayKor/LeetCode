from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def log(func):

    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        _, l1, l2 = args
        l1, l2 = l1[::-1], l2[::-1]
        return f"{l1} + {l2} = {res[::-1]}"

    return wrapped


class Solution:
    @log
    def addTwoNumbersLists(self, l1: list[int], l2: list[int]) -> list[int]:
        res = []
        tmp = 0
        n1, n2 = len(l1), len(l2)
        count = 0
        while tmp or count < max(n1, n2):
            num1 = l1[count] if count <= n1 - 1 else 0
            num2 = l2[count] if count <= n2 - 1 else 0
            tmp_sum = num1 + num2 + tmp
            tmp = 0
            if tmp_sum >= 10:
                tmp, tmp_sum = tmp_sum // 10, tmp_sum % 10
            res.append(tmp_sum)
            count += 1
        return res

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        tmp = 0
        while l1 is not None or l2 is not None or tmp:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            tmp_sum = num1 + num2 + tmp
            tmp, tmp_sum = tmp_sum // 10, tmp_sum % 10

            tail.next = ListNode(tmp_sum)
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = head.next
        # head.next = None
        return result


sol = Solution()
print(sol.addTwoNumbersLists([2, 4, 3], [5, 6, 4]))
print(sol.addTwoNumbersLists([0], [0]))
print(sol.addTwoNumbersLists([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
