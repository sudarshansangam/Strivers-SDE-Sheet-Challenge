// Given head, the head of a linked list, determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list. Otherwise, return false.

// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

// Input: head = [1,2], pos = 0
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

// Input: head = [1], pos = -1
// Output: false
// Explanation: There is no cycle in the linked list.


// SOLUTION:

// /****************************************************************

//     Following is the class structure of the Node class:

//         class Node
//         {
//         public:
//             int data;
//             Node *next;
//             Node()
//             {
//                 this->data = 0;
//                 next = NULL;
//             }
//             Node(int data)
//             {
//                 this->data = data;
//                 this->next = NULL;
//             }
//             Node(int data, Node* next)
//             {
//                 this->data = data;
//                 this->next = next;
//             }
//         };


// *****************************************************************/

bool detectCycle(Node *head)
{
	//	Write your code here
    Node* slow = head, *fast = head;
    
    while((fast != NULL)&&(fast->next != NULL)){
        fast = fast->next;
        if(fast != NULL){
            fast = fast->next;
        }
        slow = slow->next;
        if(slow == fast){
            return true;
        }
    }
    return false;
}