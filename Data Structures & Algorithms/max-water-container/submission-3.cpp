class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (r > l) {
            int sum = min(heights[l], heights[r]) * (r-l);
            max = max > sum ? max : sum;
            if (heights[r] > heights[l]) {
                l++;
            }
            else {r--;}
        }
        return max;
    }
};
