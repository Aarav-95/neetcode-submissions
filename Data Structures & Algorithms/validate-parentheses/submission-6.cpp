class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;

        for (auto i : s) {
            if ((i == '(') || (i == '[') || (i == '{')) {
                stack.push_back(i);
            }
            else {
                if (stack.size() == 0) {
                    return false;
                }
                else if (i == ')') {
                    if (stack[stack.size()-1] == '(') {
                        stack.pop_back();
                    }
                    else {
                        return false;
                    }
                }
                else if (i == '}') {
                    if (stack[stack.size()-1] == '{') {
                        stack.pop_back();
                    }
                    else {
                        return false;
                    }
                }
                else if (i == ']') {
                    if (stack[stack.size()-1] == '[') {
                        stack.pop_back();
                    }
                    else {
                        return false;
                    }
                }
            }
        }
        if (stack.size() > 0) {return false;}
        return true;
    }
};
