class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        vector<int> res;
        vector<vector<int>> ans(nums.size()+1);

        for(auto n:nums){
            m[n]++;
        }

        for(auto a:m){
            ans[a.second].push_back(a.first);
        }
        for(auto a=ans.rbegin();a!=ans.rend();++a){
            for(auto b:*a){
                res.push_back(b);
                k--;
                if(k==0)
                    return res;
            }
        }
        return res;
    }
};
