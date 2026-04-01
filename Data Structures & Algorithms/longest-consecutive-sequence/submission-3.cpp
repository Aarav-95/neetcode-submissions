class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> freq;
        int max = 0;

        for (auto i : nums) {
            freq[i]++;
        }

        for (auto i : nums) {
            vector<int> res;
            if (!freq[i-1]) {
                res.push_back(i);
                int n = 1;
                while (freq[i+n]) {
                    res.push_back(i+n);
                    n++;
                }
                max = max > res.size() ? max : res.size();
            }
        }
        return max;
    }
};
