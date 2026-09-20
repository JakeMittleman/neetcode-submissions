class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [(position[i], speed[i]) for i in range(len(position))]

        # print(fleets)
        fleets = sorted(fleets, key=lambda x: x[0])
        fleets.reverse()

        # print(fleets)

        stack = []

        for currCar in fleets:
            if not stack:
                stack.append(currCar)
                continue
                
            stackCarPos = stack[-1][0]
            stackCarSpeed = stack[-1][1]

            currCarPos = currCar[0]
            currCarSpeed = currCar[1]

            stackCarDist = (target - stackCarPos) / stackCarSpeed
            currCarDist = (target - currCarPos) / currCarSpeed

            if currCarDist <= stackCarDist:
                if currCarSpeed <= stackCarSpeed:
                    stack.pop()
                    stack.append(currCar)

            else:
                stack.append(currCar)
                
                # car makes it in time
                """
                1, 4 -> 5, 4 -> 9, 4 (10 // 4 = 2)
                3, 2 -> 5, 2 -> 9, 2 (10 // 2 = 5 )

                (4,2) will take 3 hrs to get to 10 -> 10 - 4 = 6 // 2 = 3
                (1,3) will take 5 hrs to get to 10 -> 10 - 1 = 9 // 3 = 3
                ^^ form Fleet

                (4,1) -> 6 (4, 5, 6, 7, 8, 9, 10)
                (2,3) -> 2 (2, 5, 6, 7, 8, 9, 10)
                (0,2) -> 5

                """

                # car doesn't make it in time

            # print(stack)

        return len(stack)
        