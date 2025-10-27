class Solution {
    public:
        vector<int>parent,size;
        int find_up(int node){
            if(node==parent[node])return node;
            return parent[node]=find_up(parent[node]);
        }
        void unionbysize(int u,int v){
            int up_u=find_up(u),up_v=find_up(v);
            if(up_u==up_v)return;
            if(size[up_u]>=size[up_v]){
                size[up_u]+=size[up_v];
                parent[up_v]=up_u;
            }
            else{
                size[up_v]+=size[up_u];
                parent[up_u]=up_v;
            }
        }
        vector<bool> friendRequests(int n, vector<vector<int>>& restrictions, vector<vector<int>>& requests) {
            int m=restrictions.size();
            parent.resize(n);
            size.resize(n,1);
            for(int i=0;i<n;i++)parent[i]=i;
            vector<bool>res;
            for(auto &f:requests){
                int pu=find_up(f[0]),pv=find_up(f[1]);
                bool check=true;
                for(auto &r:restrictions){
                    int ru=find_up(r[0]),rv=find_up(r[1]);
                    if((ru==pu && rv==pv)|| (ru==pv && rv==pu)){
                        check=false;
                        break;
                    }
                }
                if(check){
                    res.emplace_back(true);
                    unionbysize(f[0],f[1]);
                }
                else res.emplace_back(false);
            }
            return res;
        }
    };