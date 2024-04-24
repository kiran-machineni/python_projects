import re
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if re.match(r'^-?\d+$', op):
                scores.append(int(op))
            elif op == "C":
                scores.pop()
            elif op == "D":
                scores.append(scores[-1] * 2)
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
        return sum(scores)


my_sol = Solution()

# print(my_sol.calPoints(["5", "2", "C", "D", "+"]))
# output: 30

print(my_sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
# output: 27

# print(my_sol.calPoints((["1", "C"])))
# output: 0
