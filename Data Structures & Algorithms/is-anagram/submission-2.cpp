class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> fs;
        unordered_map<char, int> ft;

        if (s.size() != t.size()) return false;

        for (auto i : s) {
            if (fs[i]) {
                fs[i]++;
            }
            else {
                fs[i] = 1;
            }
        }

        for (auto i : t) {
            if (ft[i]) {
                ft[i]++;
            }
            else {
                ft[i] = 1;
            }
        }

        for (auto i : s) {
            if (fs[i] != ft[i]) {
                return false;
            }
        }

        return true;
    }
};
