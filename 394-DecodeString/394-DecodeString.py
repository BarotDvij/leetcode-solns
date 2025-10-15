# Last updated: 10/15/2025, 3:03:20 AM
class Solution(object):
    def decodeString(self, s):
        stack = []  # Stack to keep track of strings and multipliers
        output = ""  # Current output string
        num = ""  # Temporary variable to build the multiplier

        for i in range(len(s)):
            if s[i].isdigit():
                # Build the multiplier number (it could be more than one digit)
                num += s[i]
            elif s[i] == "[":
                # Push the current output and multiplier to the stack, then reset them
                stack.append((output, int(num)))
                output = ""
                num = ""
            elif s[i] == "]":
                # Pop from the stack and decode the current section
                last_output, multiplier = stack.pop()
                output = last_output + output * multiplier
            else:
                # Append normal characters to the current output
                output += s[i]

        return output
