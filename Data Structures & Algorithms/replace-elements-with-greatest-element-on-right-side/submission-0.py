class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n - 1):

            max_value = max(arr[i+1:])
            arr[i] = max_value
        
        arr[-1] = -1
        return arr

        