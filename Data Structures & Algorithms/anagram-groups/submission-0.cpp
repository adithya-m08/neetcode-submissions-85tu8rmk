class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> ans;
        
        for(auto str: strs){
            string key=str;
            sort(key.begin(),key.end());
            ans[key].push_back(str);
        }
        for(auto a: ans){
            res.push_back(a.second);
        }
        return res;
    }
};
