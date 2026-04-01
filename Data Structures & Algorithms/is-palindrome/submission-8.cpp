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
        int length = temp.size();
        for (int i = 0; i < length; i++) {
            if (temp[i] != temp[length - i - 1]) {
                return false;
            }
        }
        return true;
    }
};
