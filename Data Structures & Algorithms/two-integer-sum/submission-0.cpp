class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for(int i=0;i<nums.size();i++){
            int r=target-nums[i];
            if(m.find(r)!=m.end()){
                return{m[r],i};
            }
            m[nums[i]]=i;
        }
    }
};
