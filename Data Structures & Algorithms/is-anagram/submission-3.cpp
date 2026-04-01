class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freqS;
        unordered_map<char, int> freqT;

        for (int i = 0; i <= s.length(); i++) {
            freqS[s[i]]++;
            freqT[t[i]]++;
        }

        for (auto const& i : freqS) {
            if (!freqT[i.first] || i.second != freqT[i.first]) {
                return false;
            }
        }
        return true;
    }
};
