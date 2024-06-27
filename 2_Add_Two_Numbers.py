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
        res: Optional[ListNode] = ListNode(0)
        tmp = 0
        while None not in (l1, l2) or tmp:
            if l1 is None:
                num1 = 0
            else:
                num1 = l1.val
            if l2 is None:
                num2 = 0
            else:
                num2 = l2.val
            tmp_sum = num1 + num2 + tmp
            tmp = 0
            if tmp_sum >= 10:
                tmp, tmp_sum = tmp_sum // 10, tmp_sum % 10
            res.val = tmp_sum
            res.next = ListNode(0)
            res = res.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next


sol = Solution()
print(sol.addTwoNumbersLists([2, 4, 3], [5, 6, 4]))
print(sol.addTwoNumbersLists([0], [0]))
print(sol.addTwoNumbersLists([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
