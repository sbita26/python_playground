class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if stack:
                last = stack[-1]
                if self.is_pair(last, p):
                    stack.pop()
                    continue
            stack.append(p)

        return not stack
    
    def is_pair(self, last, cur):
        pairs = {'(': ')', '{': '}', '[': ']'}
        return pairs.get(last) == cur
        return False

sol = Solution()
print(sol.isValid("([{({})}])"))