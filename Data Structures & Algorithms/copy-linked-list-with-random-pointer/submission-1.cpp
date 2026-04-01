/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) {return nullptr;}
        Node* cur = head;
        Node* prev = new Node {cur->val};
        Node* temp = prev;
        unordered_map<Node*, Node*> m;
        m[cur] = prev;
        cur = cur->next;
        while (cur) {
            Node* t = new Node {cur->val};
            prev->next = t;
            m[cur] = t;
            prev = prev->next;
            cur = cur->next;
        }
        Node* a = temp;
        cur = head;
        while (temp) {
            temp->random = m[cur->random];
            temp = temp->next;
            cur = cur->next;
        }
        return a;
    }
};
