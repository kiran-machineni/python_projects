class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == "U":
                y += 1
            if move == "R":
                x += 1
            if move == "D":
                y -= 1
            if move == "L":
                x -= 1
        return x == y == 0


my_sol = Solution()

print(my_sol.judgeCircle("UU"))
# output: False

print(my_sol.judgeCircle(("URDL")))
# output: True
