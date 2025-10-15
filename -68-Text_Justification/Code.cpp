#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void addSpaces(string &str, int count) {
        for (int i = 0; i < count; i++)
            str.push_back(' ');
    }

    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        int ind = 0;
        int n = words.size();

        while (ind < n) {
            int charsLength = words[ind].length();
            int last = ind + 1;

            while (last < n) {
                if (charsLength + 1 + words[last].length() > maxWidth)
                    break;
                charsLength += 1 + words[last].length();
                last++;
            }

            int diff = last - ind - 1;
            string str = "";

            if (diff == 0 || last == n) {
                for (int i = ind; i < last; i++) {
                    str += words[i];
                    if (i < last - 1) str.push_back(' ');
                }
                int countSpaces = maxWidth - str.length();
                addSpaces(str, countSpaces);
            } else {
                int spaces = (maxWidth - charsLength) / diff;
                int remSpaces = (maxWidth - charsLength) % diff;
                for (int i = ind; i < last; i++) {
                    str += words[i];
                    if (i < last - 1) {
                        int countSpaces = spaces + (i - ind < remSpaces ? 1 : 0);
                        addSpaces(str, 1 + countSpaces);
                    }
                }
            }

            ans.push_back(str);
            ind = last;
        }

        return ans;
    }
};

int main() {
    int n, maxWidth;
    cout << "Enter number of words: ";
    cin >> n;
    vector<string> words(n);
    cout << "Enter words:\n";
    for (int i = 0; i < n; i++) cin >> words[i];
    cout << "Enter max width: ";
    cin >> maxWidth;

    Solution s;
    vector<string> result = s.fullJustify(words, maxWidth);

    cout << "\nJustified Text:\n";
    for (string &line : result)
        cout << '"' << line << '"' << endl;
}
