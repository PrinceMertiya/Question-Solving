from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        hold = set()
        key = set()
        q = deque()

        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                hold.add(box)
        candy_count = 0
        while q:
            c = q.popleft()
            candy_count += candies[c]
            for k in keys[c]:
                key.add(k)  
                if k in hold:
                    q.append(k)
                    hold.remove(k)
            for box in containedBoxes[c]:
                if status[box] == 0 and box not in key:
                    hold.add(box)

                else:
                    q.append(box)
        return candy_count                                   