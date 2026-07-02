class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ##each asteroid same speed
        ## signs - direction abs value - size
        ##when collision smaller explodes same size both explode 2 in same direction never meet
        n=len(asteroids)
        stack=[]
        for j in range(0,n):

            if asteroids[j]>0:
                stack.append(asteroids[j])
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroids[j]):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(asteroids[j])
                elif stack[-1]==abs(asteroids[j]):
                    stack.pop()
            
          
        return stack