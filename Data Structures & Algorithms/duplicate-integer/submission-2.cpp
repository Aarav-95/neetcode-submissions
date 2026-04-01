class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq;

        for (auto i : nums) {
            if (freq[i]) {
                return true;
            }
            else {
                freq[i] = 1;
            }
        }
        return false;
    }
};