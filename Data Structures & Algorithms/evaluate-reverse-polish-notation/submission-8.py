class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for t in tokens:
            if t not in "+-*/":
                s.append(t)
            else:
                a=int(s.pop())
                b=int(s.pop())
                if t=='+':
                    c=b+a
                elif t=='-':
                    c=b-a
                elif t=='*':
                    c=b*a
                else:
                    c=int(b / a)

                s.append(c)
        print(s[0])
        return int(s[0])