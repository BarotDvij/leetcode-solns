# Last updated: 1/3/2026, 2:57:40 PM
1from collections import deque
2
3class Solution:
4    def predictPartyVictory(self, senate: str) -> str:
5        # iterate over the string and add everything in the queue
6        r = deque()
7        d = deque()
8        for i in range(len(senate)):
9            if senate[i] == 'R':
10                r.append(i)
11            #else instead of e
12            #since senate is only 'R' or 'D' given in restraints
13            else:
14                d.append(i)
15        
16        while len(r) != 0 and len(d) != 0: 
17            if r[0] < d[0]:
18                d.popleft()
19                r.append(len(senate)+ r[0])
20                r.popleft()
21
22            else:
23                r.popleft()
24                d.append(len(senate)+ d[0])
25                d.popleft()
26        
27        if len(r) > 0:
28            return 'Radiant'
29        
30        else:
31            return 'Dire'