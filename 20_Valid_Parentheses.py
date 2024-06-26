class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for sym in s:
            if sym in "([{":
                stack.append(sym)
            else:
                if (
                    not stack
                    or (sym == ")" and stack[-1] != "(")
                    or (sym == "}" and stack[-1] != "{")
                    or (sym == "]" and stack[-1] != "[")
                ):
                    return False
                stack.pop()
        return not stack


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("())"))
print(sol.isValid("[()]"))
print(sol.isValid("[[[[[[[[({{}}})]]]]]]]]"))
