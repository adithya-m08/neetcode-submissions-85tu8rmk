class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}
        stack=[]
        res=False
        for a in s:
            if a in d.keys():
                stack.append(a)
            elif(stack and d[stack.pop()] == a):
                continue
            else:
                return False
        return not stack
