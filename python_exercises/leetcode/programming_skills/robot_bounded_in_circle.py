class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        angle = 0
        direction = "North"
        for _ in range(4):  # Check for up to 4 executions
            for i in instructions:
                if i == "G":
                    if direction == "North":
                        y += 1
                    elif direction == "South":
                        y -= 1
                    elif direction == "East":
                        x += 1
                    elif direction == "West":
                        x -= 1
                elif i == "R":
                    angle += 90
                    if direction == "North":
                        direction = "East"
                    elif direction == "South":
                        direction = "West"
                    elif direction == "East":
                        direction = "South"
                    elif direction == "West":
                        direction = "North"
                elif i == "L":
                    angle -= 90
                    if direction == "North":
                        direction = "West"
                    elif direction == "South":
                        direction = "East"
                    elif direction == "East":
                        direction = "North"
                    elif direction == "West":
                        direction = "South"
            if x == 0 and y == 0 and direction == "North":
                return True  # Robot returns to initial position and direction
        return False  # Robot does not return to initial position and direction after 4 executions


my_sol = Solution()

# print(my_sol.isRobotBounded("LLGRL"))
# output: True

print(my_sol.isRobotBounded("GG"))
# output: False
