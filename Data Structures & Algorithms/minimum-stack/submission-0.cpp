class MinStack {
public:
    struct Node {
        int val;
        Node* next;
    };
    Node* head;
    Node* min;
    MinStack() {
        head = nullptr;
        min = nullptr;
    }
    
    void push(int val) {
        Node* cur = new Node {};
        cur->val = val;
        cur->next = head;
        head = cur;
        
        Node* temp = new Node {};
        Node* mtemp = min;
        int add;
        if (mtemp) {
            add = mtemp->val < val ? mtemp->val : val;
        }
        else {add = val;}
        temp->val = add;
        temp->next = mtemp;
        min = temp;
    }
    
    void pop() {
        Node* temp = head;
        head = head->next;
        delete temp;

        Node* mtemp = min;
        min = min->next;
        delete mtemp;
    }
    
    int top() {
        return head->val;
    }
    
    int getMin() {
        return min->val;
    }
};
