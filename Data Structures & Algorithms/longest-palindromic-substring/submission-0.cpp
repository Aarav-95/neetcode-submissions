class Solution {
public:
    string longestPalindrome(string s) {
        string res;

        for (int i = 0; i < s.size(); i++) {
            string temp (1, s[i]);
            for (int j = i+1; j < s.size(); j++) {
                temp += s[j];
                string rev = temp;
                reverse(rev.begin(), rev.end());
                if (temp == rev && temp.size() > res.size()) {
                    res = temp;
                }
            }
        }
        if (res.size() == 0) {
            string t (1, s[0]);
            return t;
        }
        return res;
     }
};
