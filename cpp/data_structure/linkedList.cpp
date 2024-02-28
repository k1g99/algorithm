#include <iostream>
#include <set>
using namespace std;

struct Node{
    int data;
    Node* next;
};

class LinkedList {
    private: 
        Node* head;
        Node* tail;

    public:
        LinkedList(){
            head = nullptr;
            tail = nullptr;
        };

        void insert(int n){
            Node* newNode = new Node;
            newNode->data = n;
            newNode->next = nullptr;
            
            if(head == nullptr){
                head = newNode;
                tail = newNode;
            }else {
                tail->next = newNode;
                tail = tail->next;
            }
        }

        void print(){
            Node* ptr = head;

            while(ptr != nullptr){
                cout << ptr->data << " ";
                ptr = ptr->next;
            }

            cout << "\n";
        }
};

int main() {
    
    LinkedList ll = LinkedList();
    ll.insert(1);
    ll.insert(2);
    ll.insert(3);
    ll.insert(4);
    ll.insert(2);
    ll.print();


    return 0;
}