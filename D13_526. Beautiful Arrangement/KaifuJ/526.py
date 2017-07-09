import collections


class Solution(object):
    def __init__(self):
        self.count = 0
        self.length = 0

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        can_use = [True] * (N + 1)
        self.length = N
        self.DFS(N, can_use)
        return self.count

    def DFS(self, position, can_use):
        if position == 0:
            self.count += 1
            return
        for i in range(1, self.length + 1):
            if can_use[i] and (position % i == 0 or i % position == 0):
                can_use[i] = False
                self.DFS(position - 1, can_use)
                can_use[i] = True
        return


a = Solution()
b = a.countArrangement(3)
print(b)
