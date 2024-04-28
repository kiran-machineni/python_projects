from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # If there are only two or fewer points, they always form a straight line.
        if len(coordinates) <= 2:
            return True

        # Extracting the coordinates of the first two points.
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        # Checking if the slope between the current point and the first point
        # is equal to the slope between the second point and the first point.
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if (x1 - x0) * (yi - y0) != (xi - x0) * (y1 - y0):
                # If the slopes are not equal, the points do not form a straight line.
                return False
        # If all points have equal slopes with respect to the initial point, they form a straight line.
        return True


my_sol = Solution()
print(my_sol.checkStraightLine(([[0, 0], [0, 1], [0, -1]])))
