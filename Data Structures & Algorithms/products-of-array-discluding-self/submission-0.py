from typing import List

class Solution:
    def productExceptSelf(self,arr):
        n =len(arr)
    
        postfix =[1]*n
        prefix=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*arr[i-1]

        for i in range(n-2,-1,-1):
            postfix[i]=postfix[i+1]*arr[i+1]
        result=[0]*n
        for i in range(n):
            result[i]=postfix[i]*prefix[i]
        return result
            
        
                
    
    