class Solution {
public:
    int maxRepeating(string sequence, string word) {
        int count=0;
        string temp=word;
        while(sequence.find(temp)!=string::npos)
        {
            count++;
            temp+=word;
        }
        return count;
    }
};