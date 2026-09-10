class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # positive = -->
        # negative = <--
        stack = []

        for a in asteroids:
            if not stack or (stack[-1] * a > 0) or (stack[-1] < 0 and a > 0):
                stack.append(a)
                continue

            app = False
            while stack and stack[-1] > 0 and a < 0:
                ssize = abs(stack[-1])
                asize = abs(a)
                if ssize < asize:
                    stack.pop()
                    app = True
                elif ssize == asize:
                    stack.pop()
                    app = False
                    break
                else:
                    app = False
                    break

            if app:
                stack.append(a)

        return stack

        


