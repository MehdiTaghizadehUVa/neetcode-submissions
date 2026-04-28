class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        pointer = 0
        if n==0:
            return True
        for i in range(m):
                if t[i] == s[pointer]:
                    pointer +=1
                if pointer == n:
                    return True
        return False