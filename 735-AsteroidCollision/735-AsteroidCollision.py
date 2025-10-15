# Last updated: 10/15/2025, 3:03:11 AM
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            # Process current asteroid
            while stack and asteroid < 0 < stack[-1]:
                # Collision case
                if stack[-1] < -asteroid:
                    stack.pop()  # The last asteroid in the stack is destroyed
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both asteroids destroy each other
                break
            else:
                # No collision, add the asteroid to the stack
                stack.append(asteroid)
        
        return stack
