class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // (freq, val)
        priority_queue<pair<int, int>> heap;

        unordered_map<int, int> freq;

        for (auto i : nums) {
            freq[i]++;
        }

        for (auto& i : freq) {
            heap.push({i.second*-1, i.first*-1});
            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<int> res;

        for (int i = 0; i < k; i++) {
            res.push_back(heap.top().second * -1);
            heap.pop();
        }
        return res;
    }
};
