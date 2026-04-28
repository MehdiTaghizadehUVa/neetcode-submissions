class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        max_l = 0
        nums.sort()
        right = 0
        curr = nums[0]
        while right < len(nums):
            if curr != nums[right]:
                left = 0
                curr = nums[right]
            while right < len(nums) and nums[right]==curr:
                right +=1
            left +=1
            curr+=1
            max_l = max(max_l, left)
        return max_l

        