class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps=list(zip(position, speed))
        ps.sort(reverse=True, key=lambda x:x[0])

        stack=[]

        for p,s in ps:
            t=(target-p)/s
            if stack and t<=stack[-1]:
                continue
            else:
                stack.append(t)
        return len(stack)