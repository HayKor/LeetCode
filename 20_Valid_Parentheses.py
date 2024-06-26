class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for sym in s:
            stack.append(sym)
            if len(stack) >= 2:
                for_check = "".join(stack[-2:])
                if for_check in ["()", "{}", "[]"]:
                    stack = stack[:-2]

        return not stack


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("())"))
print(sol.isValid("[()]"))
print(sol.isValid("[[[[[[[[({{}}})]]]]]]]]"))
