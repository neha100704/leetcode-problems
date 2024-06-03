class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == "__main__":
    solution = Solution()
    n = 5  # Example input
    result = solution.climbStairs(n)
    print(f"Number of ways to climb {n} stairs: {result}")
