class Solution {
public:
    int helperRob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        int p = nums[0];
        int n = nums[1];

        for (int i = 2; i < nums.size(); i++) {
            int add = p + nums[i];
            p = p > n ? p : n;
            n = add;
        }
        return p > n ? p : n;
    }

    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        vector<int> f(nums.begin(), nums.end()-1);
        vector<int> l(nums.begin()+1, nums.end());

        int a = helperRob(f);
        int b = helperRob(l);
        return a > b ? a : b;
    }
};
