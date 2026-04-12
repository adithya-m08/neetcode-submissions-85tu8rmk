class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> r(9);
        vector<unordered_set<char>> c(9);
        vector<unordered_set<char>> box(9);

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char n=board[i][j];
                if(n!='.'){
                    int b=(i/3)*3 + j/3;
                    if(r[i].count(n) || c[j].count(n) || box[b].count(n)){
                        return false;
                    }
                    r[i].insert(n);
                    c[j].insert(n);
                    box[b].insert(n);
                }
            }
        }

        return true;
    }
};
