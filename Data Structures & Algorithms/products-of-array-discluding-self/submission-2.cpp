class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        vector<int> suffix;
        int len = nums.size();
        int run = 1;
        for (auto i : nums) {
            prefix.push_back(run);
            run = run * i;    
        }

        run = 1;
        for (int i = len - 1; i >= 0; i--) {
            suffix.push_back(run);
            run = run * nums[i];
        }

        vector<int> res;

        for (int i = 0; i < len; i++) {
            res.push_back(prefix[i] * suffix[len-i-1]);
        }
        return res;
    }
};
