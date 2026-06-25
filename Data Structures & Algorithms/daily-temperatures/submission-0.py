class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                     # stores indices
        res = [0] * len(temperatures)

        n = len(temperatures)

        for r in range(n):

            while stack and temperatures[r] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = r - idx

            stack.append(r)

        return res