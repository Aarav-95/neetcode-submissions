class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int l = 0;
        int r = 1;
        int length = prices.size();
        while (r < length) {
            res = max(res, prices[r] - prices[l]);
            if (prices[r] <= prices[l]) {
                l = r;
                r++;
            }
            else {
                r++;
            }
        }
        return res;
    }
};
