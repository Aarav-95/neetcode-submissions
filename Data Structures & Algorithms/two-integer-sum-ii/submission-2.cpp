class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        vector<int> res;
        while (r > l) {
            int sum = numbers[r] + numbers[l];
            if (sum == target) {
                res.push_back(l+1);
                res.push_back(r+1);
                return res;
            }
            else if (sum > target) {
                r--;
            }
            else {
                l++;
            }
        }
    }
};
