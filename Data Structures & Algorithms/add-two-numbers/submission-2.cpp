/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        int num, a, b = 0;
        int carry = 0;
        while (cur1 && cur2) {
            a = cur1->val;
            b = cur2->val;
            num = (a + b) % 10;
            cur2->val = num + carry;
            carry = (a + b) / 10;
            cur1 = cur1->next;
            cur2 = cur2->next;
        }
        if (cur1) {
            cur2 = l2;
            while (cur2->next) {cur2 = cur2->next;}
            cur2->next = cur1;
            cur2 = cur2->next;
            cur2->val += carry;
            if (cur2 && cur2->val >= 10) {
                while (cur2 && cur2->val >= 10) {
                carry = cur2->val / 10;
                cur2->val %= 10;
                cur2 = cur2->next;
                if (!cur2) break;
                cur2->val += carry;
                carry = 0;
                }
            }
            else {carry = 0;}
        }
        else if (cur2) {
            cur2->val += carry;
            if (cur2 && cur2->val >= 10) {
                while (cur2 && cur2->val >= 10) {
                carry = cur2->val / 10;
                cur2->val %= 10;
                cur2 = cur2->next;
                if (!cur2) break;
                cur2->val += carry;
                carry = 0;
                }
            }
            else {carry = 0;}
        }
        if (carry > 0) {
            cur2 = l2;
            while (cur2->next) {cur2 = cur2->next;}
            cur2->next = new ListNode{carry};
        }
        return l2;
    }
};
