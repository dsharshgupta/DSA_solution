from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Becuase if k = 8 and length = 7, means
        # we should only rotate 1 time instead of 8 times
        rotations = k % len(nums)

        for _ in range(rotations):
            last = nums.pop()
            nums.insert(0, last)