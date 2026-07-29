class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequencies = defaultdict(int)

        left = 0
        best = 0

        for right, char in enumerate(s):
            frequencies[char] += 1

            while frequencies[char] > 1:
                frequencies[s[left]] -= 1
                left +=1
            best = max(best, right - left + 1)
        
        return best