class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_p = {')':'(', '}':'{', ']':'['}
        if len(s) <2:
            return False
        for char in s:
            if char in map_p:
                if stack:
                    prev = stack.pop()
                    if prev != map_p[char]:
                        return False
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return len(stack) == 0