class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:

            m = (l + r) // 2
            # print("max_weight: {0} | day_count: {1}".format(m, day_count))

            if canShip(m):
                res = min(res, m)
                r = m-1

            else:
                l = m+1

        return res


