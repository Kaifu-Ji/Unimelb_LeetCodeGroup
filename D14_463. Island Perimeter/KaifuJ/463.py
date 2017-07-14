import operator


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        v = [sum(list(map(operator.ne, row + [0], [0] + row))) for row in grid]
        h = [sum(list(map(operator.ne, row + [0], [0] + row))) for row in map(list, zip(*grid))]
        return sum(v) + sum(h)


a = Solution()
print(a.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
