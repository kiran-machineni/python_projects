class Solution:
    """
    Provides a method to validate balanced parentheses in a string.
    """

    def isValid(self, s: str) -> bool:
        """
        Determines if the parentheses in a string are balanced.

        Args:
            s: The string to be checked for balanced parentheses.

        Returns:
            True if the parentheses are balanced, False otherwise.
        """

        stack = []
        matching_pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in matching_pairs.values():
                stack.append(char)
            elif char in matching_pairs.keys():
                if not stack or matching_pairs[char] != stack.pop():
                    return False
            else:
                pass  # Ignore characters that aren't parentheses
        return len(stack) == 0

solution_instance = Solution()
result = solution_instance.isValid("1()[]")
print(result)
