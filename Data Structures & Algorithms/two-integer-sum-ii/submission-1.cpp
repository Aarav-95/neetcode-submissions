class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;

        while (r >= l) {
            int temp = numbers[l] + numbers[r];
            if (temp == target) {
                return vector<int> {l+1, r+1};
            }
            else if (temp > target) {
                r -= 1;
            }
            else {
                l += 1;
            }
        }
    }
};
