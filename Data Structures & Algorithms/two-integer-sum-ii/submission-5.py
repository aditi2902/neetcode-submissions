class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pos=[]
        sum=0
        start=0
        end=len(numbers)-1
        while  start<end:
            sum=numbers[start]+numbers[end]
            if sum>target:
                end-=1
            elif sum<target:
                start+=1
            else:
                break
        pos.append(start+1)
        pos.append(end+1)
        return pos
