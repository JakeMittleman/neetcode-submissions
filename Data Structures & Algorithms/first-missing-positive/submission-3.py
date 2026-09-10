class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                indx = abs(nums[i]) - 1
                if indx < len(nums):
                    if nums[indx] == 0:
                        nums[indx] = -(len(nums) + 1)
                    else:
                        nums[indx] = -abs(nums[indx])

        # res = len(nums) + 1
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i

        # print(nums)
        return len(nums) + 1