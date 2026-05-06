class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l
        def BS(l, r):

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1

        if nums[pivot] <= target <= nums[n - 1]:
            return BS(pivot, n - 1)
        else:
            return BS(0, pivot)
