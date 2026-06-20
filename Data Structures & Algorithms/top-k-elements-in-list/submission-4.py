class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for _ in range(len(nums)+1)]

        for key, c in count.items():
            freq[c].append(key)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return res