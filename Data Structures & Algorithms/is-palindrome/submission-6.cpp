class Solution {
public:
    bool isPalindrome(string s) {
        string res;
        for (auto i : s) {
            if (isalnum(i)) {
                res += tolower(i);
            }
        }
        string rev = res;
        reverse(rev.begin(), rev.end());
        cout << rev;
        if (rev == res) return true;
        return false;
    }
};
