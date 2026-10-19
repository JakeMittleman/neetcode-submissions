class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        def count_hours(rate):
            hours = 0
            for pile in piles:
                hours += pile // rate + 1 if pile % rate != 0 else pile // rate

            return hours

        while l <= r:

            m = (l + r) // 2
            hours = count_hours(m)
            print(hours, m)

            if hours > h:
                l = m+1

            elif hours <= h:
                r = m-1

        return l

