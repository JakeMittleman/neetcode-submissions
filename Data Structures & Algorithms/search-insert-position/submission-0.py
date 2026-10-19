class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def bs(l, r):
            if l > r:
                return l

            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                return bs(l, r-1)

            else:
                return bs(m+1,r)

        return bs(0, len(nums)-1)