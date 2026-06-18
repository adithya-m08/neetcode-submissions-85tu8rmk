class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')', '{':'}', '[':']'}
        stack=[]

        for a in s:
            if a in d.keys():
                stack.append(a)
            else:
                if not stack:
                    return False
                b=stack.pop()
                if d[b]!=a:
                    return False
        return not len(stack)