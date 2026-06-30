class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ##cant beat the car in front
        ##Only catch up
        time=[0]*len(position)
        count = 0
        for i in range(len(position)):
            time[i]=(target-position[i])/speed[i]
        ##Important
        cars=list(zip(position,time))
        cars.sort()
        ## find number of fleets at destination
        stack=[] ##push only fleet time 
        
        for i in range(len(cars)-1,-1,-1):
            if not stack:
                stack.append(cars[i][1])
            if stack[-1]>=cars[i][1]:
                continue
            else :
                stack.append(cars[i][1])
                count+=1
        return len(stack)
        
            


        

    
            


