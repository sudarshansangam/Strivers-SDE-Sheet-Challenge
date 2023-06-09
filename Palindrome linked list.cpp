// Given the head of a singly linked list, return true if it is a 
// palindrome
//  or false otherwise.

// Example 1:

// Input: head = [1,2,2,1]
// Output: true

// Example 2:

// Input: head = [1,2]
// Output: false

// SOLUTION:

#include <bits/stdc++.h> 
/****************************************************************

    Following is the class structure of the LinkedListNode class:

    template <typename T>
    class LinkedListNode
    {
    public:
        T data;
        LinkedListNode<T> *next;
        LinkedListNode(T data)
        {
            this->data = data;
            this->next = NULL;
        }
    };

*****************************************************************/

bool isPalindrome(LinkedListNode<int> *head) {
    // Write your code here.
    stack<int> s;
    LinkedListNode<int>* th = head;

    while(th != NULL){
        s.push(th->data);
        th = th->next;
    }
    th = head;
    while(!s.empty()){
        if(s.top() != th->data){
            return false;
        }
        s.pop();
        th = th->next;
    }
    return true;

}