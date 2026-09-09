from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        counts = defaultdict(int)
        counts[0] = 1
        res = 0

        # 2, -1, 1, 2
        # 2, 1, 2, 4

        for num in nums:
            prefix += num
            if prefix - k in counts:
                res += counts[prefix-k]

            counts[prefix] += 1

        return res