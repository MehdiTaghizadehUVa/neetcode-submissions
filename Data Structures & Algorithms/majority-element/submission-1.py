
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_hash = defaultdict(int)
        ans = 0
        max_Count = 0
        for num in nums:
            count_hash[num] +=1
            if count_hash[num] > max_Count:
                max_Count = count_hash[num]
                res = num


        return res
