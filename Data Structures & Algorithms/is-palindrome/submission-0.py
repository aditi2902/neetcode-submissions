class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        rev=""
        s=s.lower()
        for x in s:
            if x.isalnum():
                temp+=x
        for x in s[::-1]:
            if x.isalnum():
                rev+=x
        if temp==rev:
            return True
        else:
            return False
    
