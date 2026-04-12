class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=list(zip(position,speed))
        pairs.sort(reverse=True)

        stack=[]

        for c in pairs:
            t=(target-c[0])/c[1]
            if stack and t<=stack[-1]:
               continue
            else: 
                stack.append(t)

        return len(stack)