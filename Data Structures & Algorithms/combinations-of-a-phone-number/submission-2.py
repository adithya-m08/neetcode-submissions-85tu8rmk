class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        if digits=='':
            return []
        def dfs(i, char):
            if i >=len(digits):
                res.append(char)
                return

            for s in phone[digits[i]]:
                dfs(i+1,char+s)
        dfs(0, '')
        return res