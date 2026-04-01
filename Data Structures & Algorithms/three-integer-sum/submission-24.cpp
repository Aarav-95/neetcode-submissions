class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int length = nums.size();
        vector<vector<int>> res;
        for (int i = 0; i < length - 1; i++) {
            int target = nums[i] * -1;
            int l = i + 1;
            int r = length - 1;
            while (r > l) {
                if (nums[r] + nums[l] == target) {
                    res.push_back({nums[l], nums[r], nums[i]});
                    l++;
                    r--;
                    while (l < length - 1 && nums[l-1] == nums[l]) {
                        l++;
                    }
                    while (r > i && nums[r] == nums[r+1]) {
                        r--;
                    }
                }
                else if (nums[r] + nums[l] > target) {
                    r--;
                    while (r > i && nums[r] == nums[r+1]) {
                        r--;
                    }
                }
                else {
                    l++;
                    while (l < length - 1 && nums[l] == nums[l-1]) {
                        l++;
                    }
                }
            }
            while (i < length - 1 && nums[i] == nums[i+1]) {
                i++;
            }
        }
        return res;
    } 
};
