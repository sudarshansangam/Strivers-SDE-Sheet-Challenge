/*
Following is the class structure of the Node class:

class Node
{
public:
    int data;
    Node *next;
    Node()
    {
        this->data = 0;
        next = NULL;
    }
    Node(int data)
    {
        this->data = data; 
        this->next = NULL;
    }
    Node(int data, Node* next)
    {
        this->data = data;
        this->next = next;
    }
};
*/

Node* removeKthNode(Node* head, int k)
{
    // Write your code here.
    Node* slow = head, *fast = head, *prev = NULL;

    for(int i=0; i<k; i++){
        fast = fast->next;
    }

    while(fast != NULL){
        prev = slow;
        slow = slow->next;
        fast = fast->next;
    }
    if(prev==NULL) return head->next;
    prev->next = slow->next;
    return head;
}