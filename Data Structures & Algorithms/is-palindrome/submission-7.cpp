class Solution {
public:
    bool isPalindrome(string s) {
        string temp = "";

        for (auto i : s) {
            char character = tolower(i);
            if (isalnum(character)) {
                temp = temp + character;
            }
        }

        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] != temp[temp.size() - i - 1]) {
                return false;
            }
        }
        return true;
    }
};
