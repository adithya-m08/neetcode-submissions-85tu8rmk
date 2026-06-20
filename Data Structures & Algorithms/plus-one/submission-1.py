class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def f(i):
            nonlocal digits
            digits[i]+=1
            if digits[i]>9:
                if i==0:
                    digits[i]=0
                    digits=[1]+digits
                    return
                digits[i]=0
                f(i-1)
            return
            
        f(len(digits)-1)
        return digits