from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_hash = Counter(nums)
        l = len(nums) // 2
        for num in count_hash:
            if count_hash[num] > l:
                return num
