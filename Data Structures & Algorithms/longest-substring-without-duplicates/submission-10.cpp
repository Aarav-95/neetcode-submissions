class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0, l = 0, r = 0, length = s.size();
        unordered_map<char, int> freq;
        while (r < length) {
            if (freq.contains(s[r]) && freq[s[r]] >= l) {
                res = max(res, r-l);
                l = freq[s[r]] + 1;
                freq[s[r]] = r;
            }
            else {
                freq[s[r]] = r;
            }
            r++;
            if (r == 6) {cout << freq[s[r]] << endl;}
        }
        return max(res, r-l);
    }
};
