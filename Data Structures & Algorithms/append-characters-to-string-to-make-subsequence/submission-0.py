class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = 0
        n = len(s)
        m = len(t)

        for i in range(n):
            if s[i] == t[left]:
                left +=1
            if left >= m:
                return 0
        return m - left