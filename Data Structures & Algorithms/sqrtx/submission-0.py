class Solution:
    def mySqrt(self, x: int) -> int:
        
        def bs(l, r):
            if l > r:
                return r

            m = (l+r) // 2
            if m * m == x:
                return m

            elif m*m > x:
                return bs(l, m-1)

            else:
                return bs(m+1, r)

        return bs(1, x)