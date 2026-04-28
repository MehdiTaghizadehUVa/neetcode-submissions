class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Write your code here
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                temp_sum = nums[left] + nums[right]
                if temp_sum < target:
                    left += 1
                elif temp_sum > target:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1

        return ans
