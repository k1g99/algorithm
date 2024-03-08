#include <iostream>
#include <vector>
#include <list>
#include <iterator>

using namespace std;
/*
list : doubly linked list
forward_list : single linked list

list VS vector
    + list : cheap instertion/deletion in the middle
    + vector : fast random access, cheap insertion/deletion in the end
*/

int main() {
    list<int> li = {3, 5, 7};
    
    li.emplace_back(9);
    li.emplace_front(1);


    for (auto iter: li){
        cout << iter << " ";
    }
    cout << "\n";

    auto it = li.begin();
    auto add_it = next(it, 1);
    li.insert(add_it, 2);

    for (auto iter: li){
        cout << iter << " ";
    }
    cout << "\n";

    list<int> li2 = {4,4,4,4,4};
    add_it = next(it, 3);
    li.insert(add_it, li2.begin(), li2.end());

    for (auto iter: li) {
        cout << iter << " ";
    }
    cout << "\n";


    return 0;
}