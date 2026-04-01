class Solution {
public:
    int trap(vector<int>& height) {
        int length = height.size();
        vector<int> leftMax;
        vector<int> rightMax;
        int run = 0;
        int total = 0;
        for (int i{0}; i < length; i++) {
            leftMax.push_back(run);
            run = height[i] > run ? height[i] : run;
        }
        run = 0;
        for (int i{length - 1}; i >= 0; i--) {
            rightMax.push_back(run);
            run = height[i] > run ? height[i] : run;
        }

        for (int i{0}; i < length; i++) {
            int sum = min(leftMax[i], rightMax[length-i]) - height[i];
            if (sum > 0) {
                total += sum;
            }
        }
        return total;
    }
};
