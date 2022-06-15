# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Difficulty : Medium
"""

"""
Solution:
    If we start with the two lines furthest apart, we know that the length for the combination is the maximum it can be
    With this information, we know that the largest area is now constrained by the lower of the two vertical lines.
    For that particular lowest vertical line, the area calculated is already the largest area.
    We should now move inward from the vertical line to see if we can find the largest container
    
"""
class Solution:    

    def maxArea(self, height: list) -> int:
        #holds maximum area of water
        maxWater = 0
        
        #two pointers, one starting at index 0, other at last index of the list
        leftwall, rightwall = 0, len(height) - 1
        
        #iterate through until both left and right are one away from each other
        while leftwall < rightwall:
            maxWater = max(maxWater, min(height[leftwall], height[rightwall]) * (rightwall - leftwall))
            
            #increasing whichever pointer has a smaller line, we want to maximize the area
            if height[leftwall] <= height[rightwall]:
                leftwall += 1
            else:
                rightwall -= 1
        
        return maxWater

def main():
    heights =  [0,1,2,3,4,5,6,7,8,9,1,1,9]
    S = Solution()
    A = S.maxArea(heights)
    print(A)
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()