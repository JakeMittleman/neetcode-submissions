class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        res = 1001

        while l <= r:

            m = (l+r) // 2

            res = min(res, nums[m])

            # are we in the right or left half

            # we're in the left half (m > right-most)

            # we're in the right half (m < left-most)
            if nums[m] < nums[r]:
                r = m-1

            else:
                l = m+1

        return res

        
        