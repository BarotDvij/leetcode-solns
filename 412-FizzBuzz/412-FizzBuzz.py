# Last updated: 10/15/2025, 3:03:19 AM
class Solution(object):
    def fizzBuzz(self, n):
        output = []
        for i in range(1, n+1):
            output.append(str(i))

        for m in range(3, n+1, 3):
            output[m-1] = "Fizz"

        for o in range(5, n+1, 5):
            output[o-1] = "Buzz"

        for p in range(15, n+1, 15):
            output[p-1] = "FizzBuzz"

        return output