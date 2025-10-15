# Last updated: 10/15/2025, 3:03:18 AM
class Solution(object):
    def compress(self, chars):
        s = []
        i = 0
        count = 1  # Start count at 1

        if len(chars) < 2:
            return len(chars)

        for i in range(len(chars)):
            # Check for consecutive characters
            if i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
            else:
                # Append character to compressed list
                s.append(chars[i])

                # If count > 1, append each digit of the count separately
                if count > 1:
                    for digit in str(count):
                        s.append(digit)

                # Reset count after completing a group
                count = 1

        # Write back the compressed list to chars and return the new length
        chars[:len(s)] = s
        return len(s)
