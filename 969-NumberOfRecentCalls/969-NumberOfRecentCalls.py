# Last updated: 10/15/2025, 3:03:11 AM
class RecentCounter(object):
    def __init__(self):
        self.times = deque()

    def ping(self, t):
        self.times.append(t)

        while self.times[0] < t - 3000: 
            self.times.popleft()
        
        return len(self.times)
        """
        :type t: int
        :rtype: int
        """
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)