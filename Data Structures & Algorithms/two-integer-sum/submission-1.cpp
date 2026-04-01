class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> n;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            if (n.contains(target - nums[i])) {
                res.push_back(n[target-nums[i]]);
                res.push_back(i);
                return res;
            }
            n[nums[i]] = i;
        }
        return res;
    }
};
