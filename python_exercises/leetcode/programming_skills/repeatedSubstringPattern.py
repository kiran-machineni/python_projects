class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        # Check for all possible substrings starting from length 1 up to half the length of the string
        for i in range(1, len(s) // 2 + 1):
            # If the length of the string is divisible by the current substring length
            if length % i == 0:
                # Extract the current substring
                substring = s[:i]
                # If repeating the substring generates the original string, return True
                if substring * (length // i) == s:
                    return True
        return False


my_sol = Solution()

print(my_sol.repeatedSubstringPattern("ababc"))
