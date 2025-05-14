class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n =len(heights)
        stack = []
        max_value = 0

        for i in range(n + 1):
            currentheight = 0 if i == n else heights[i]
            while stack and currentheight < heights[stack[-1]] :
                height = heights[stack.pop()]
                width =  i if not stack else i - stack[-1]  -1 
                max_value = max(max_value ,height * width)
            stack.append(i)   

        return max_value    