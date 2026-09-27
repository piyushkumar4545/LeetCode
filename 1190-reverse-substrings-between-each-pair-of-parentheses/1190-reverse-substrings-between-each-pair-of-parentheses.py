class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                part = stack.pop()[::-1]
                if stack:
                    stack[-1].extend(part)
                else:
                    stack.append(part)
            else:
                if stack:
                    stack[-1].append(ch)
                else:
                    stack.append([ch])

        return ''.join(stack[-1])