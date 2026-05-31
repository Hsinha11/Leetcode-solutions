class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& ast) {
        int m = mass;
        int maxi = *max_element(ast.begin(),ast.end());
        sort(ast.begin(),ast.end());
        for(auto i:ast){
            if (m<i) return false;
            else{
                m+=i;
                if (m>=maxi) {
                    return true;
                }
            }
        }
        return true;
    }
};