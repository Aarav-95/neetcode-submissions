class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (auto i : strs) {
            string length = to_string(i.size());
            res += length + "_" + i;
        }
        cout << res;
        return res;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> res;
        while (i < s.size()) {
            string temp = "";
            string w = "";
            while (temp != "_") {
                w += s[i];
                i++;
                temp = s[i];
            }
            int wordSize = stoi(w);
            string word = "";
            i++;
            for (int j = 0; j < wordSize; j++) {
                word += s[i];
                i++;
            }
            res.push_back(word);
            word = "";
        }
        return res;
    }
};
