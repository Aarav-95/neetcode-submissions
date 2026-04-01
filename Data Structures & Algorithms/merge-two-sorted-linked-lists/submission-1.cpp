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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* l1 = list1;
        ListNode* l2 = list2;
        ListNode* cur = new ListNode {};
        ListNode* temp = cur;
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            }
            else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        if (l1 == nullptr) {
            while (l2 != nullptr) {
                cur->next = l2;
                cur = cur->next;
                l2 = l2->next;
            }
        }
        else if (l2 == nullptr) {
            while (l1 != nullptr) {
                cur->next = l1;
                cur = cur->next;
                l1 = l1->next;
            }
        }
        return temp->next;
    }
};
