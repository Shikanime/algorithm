from .three_sum import Solution


def test_solution():
    solver = Solution()
    assert solver.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
