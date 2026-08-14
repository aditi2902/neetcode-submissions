class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def func(index, subset):
            total = sum(subset)

            if total == target:
                res.append(subset.copy())
                return

            if index >= len(nums) or total > target:
                return

            # Take current number AGAIN
            subset.append(nums[index])
            func(index, subset)
            subset.pop()

            # Don't take current number
            func(index + 1, subset)

        func(0, [])
        return res