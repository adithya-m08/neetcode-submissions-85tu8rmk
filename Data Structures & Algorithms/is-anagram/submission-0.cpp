class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
            return false;
        
        unordered_map<char,int> m;
        unordered_map<char,int> n;
        for(int i=0;i<s.length();i++){
            m[s[i]]++;
            n[t[i]]++;
        } 
        return m==n;
    }
};
