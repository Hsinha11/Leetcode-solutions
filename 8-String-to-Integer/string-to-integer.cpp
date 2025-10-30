#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int f=1, i=0, n=s.size();
        long long num=0;
        while(i<n && s[i]==' '){
            i++;
        }
        if(s[i] == '-'){
            f = f*-1;
            i++;
        }
        else if(s[i] == '+'){
            i++;
        }
        while(isdigit(s[i])){
            num = num*10 + (s[i]-'0');
            if(num>INT_MAX && f==-1)
                return INT_MIN;
            else if(num>INT_MAX && f==1)
                return INT_MAX;
            i++;
        }
        return num*f;
    }
};