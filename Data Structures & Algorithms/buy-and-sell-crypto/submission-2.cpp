class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int max = 0;

        while (r < prices.size() && r >= l) {
            max = max > prices[r] - prices[l] ? max : prices[r] - prices[l];
            if (prices[r] > prices[l]) {
                r += 1;
            }
            else {
                l = r;
                r += 1;
            }
        }
        return max;
    }
};
