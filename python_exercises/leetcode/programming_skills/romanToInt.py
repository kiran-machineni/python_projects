class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and symbol_values[s[i]] < symbol_values[s[i + 1]]:
                result -= symbol_values[s[i]]
            else:
                result += symbol_values[s[i]]
        return result


my_sol = Solution()

print(my_sol.romanToInt("LVIII"))
