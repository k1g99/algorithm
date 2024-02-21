#include <iostream>
#include <vector>
#include <deque>

using namespace std;

/*
deque VS vector
- the elements of a deque are not stored contiguously

Random access - constant O(1).
Insertion or removal of elements at the end or beginning - constant O(1).
Insertion or removal of elements - linear O(n).
*/

int main() {
    deque<int> dq = {3, 5, 7};

    dq.emplace_back(9);
    dq.emplace_front(1);

    for (auto iter: dq){
        cout << iter << " ";
    }
    cout << "\n";

    dq.pop_front();
    dq.pop_back();

    for (auto iter: dq){
        cout << iter << " ";
    }
    cout << "\n";

    return 0;
}