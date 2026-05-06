class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        p_index = l
        def BS(arr):
            l = 0
            r = len(arr) -1

            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < target:
                    l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1

        start_l = 0
        end_l = p_index
        start_r = p_index
        end_r = len(nums) - 1
        if nums[start_r] <= target <= nums[end_r]:
            return BS(nums[start_r:]) + p_index if BS(nums[start_r:])>= 0 else -1
        else:
            return BS(nums[start_l:end_l])
