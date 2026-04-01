class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> freq;
        int res = 0;
        for (auto i : nums) {
            freq[i]++;
        }

        while (nums.size() > 0) {
            int count = 1;
            int temp = 1;
            while (freq[nums[0] - count]) {
                count++;
            }
            int lowest = nums[0] - count + 1;
            count = 1;
            while (freq[lowest + count]) {
                temp++;
                erase(nums, lowest + count);
                count++;
            }
            res = res > temp ? res : temp;
            erase(nums, lowest);
        }
        return res;
    }

};
