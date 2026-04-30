class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left_bound = stack[-1] if stack else -1
                right_bound = i
                width = right_bound - left_bound - 1
                area = height * width
                max_area = max(max_area, area)

            stack.append(i)
        return max_area