class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # left to right 
        # final ans is min value of stored sums of index 1 or 0
        # destination is your top value+1
        cost.append(0) # let desitination have value 0
        for i in range(len(cost)-3,-1,-1): # len(cost)-3 is the index which on +2 will give the extra value beyond that index out of bounds for +2
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])