class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        """
        


        want to go right, how do we know that?

        m = 3

        if m == target:
            return m

        if m > r (in the left half)
           if m < target:
               l = m + 1
            
            if m > target and target > l:
                r = m - 1

            if m > target and l > target:
                l = m + 1

        if m < r (in the right half)
            if target < m:
                r = m - 1

            if target > m and target <= r:
                l = m + 1

            if target > m and target > r:
                r = m - 1



         lr
        [3, 5, 6, 0, 0, 1, 2] target = 4 

         l     m     r
        [2, 2, 4, 5, 2] currently in left half
        [1, 0, 1, 1, 1] currently in right half
        """

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l+r)//2

            if nums[m] == target:
                return True

            # left sorted half
            if nums[m] > nums[l]:
                # target still in left half
                if target < nums[m] and target >= nums[l]:
                    r = m-1

                else:
                    l = m+1

            # right sorted half
            elif nums[m] < nums[l]:
                # target is to the left
                if nums[m] > target or (nums[m] < target and target >= nums[l]):
                    r = m-1

                # case 1: Target still in right half
                else:
                    l = m+1

            else:
                l += 1

        return False

            

            # if m == r, then l >= r

            # in the left half
            # if nums[m] > nums[r] or (nums[m] == nums[r] and nums[m] > nums[l]):
            #     if nums[m] < target or (nums[m] > target and nums[l] > target):
            #         l = m+1

            #     elif nums[m] > target and target >= nums[l]:
            #         r = m-1

            # # in the right half
            # elif nums[m] > nums[l]:
            #     if nums[m] > target or (nums[m] < target and nums[r] < target):
            #         r = m-1

            #     elif nums[m] < target and nums[r] >= target:
            #         l = m+1

            # elif nums[m] == nums[r] and nums[m] == nums[l]:
            #     l += 1
            #     r -= 1











