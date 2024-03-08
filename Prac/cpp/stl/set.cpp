#include <iostream>
#include <vector>
#include <set>

using namespace std;

/*
base : RB Tree

set : sorted set of unique objects (no duplicated value)
multi-set : allows duplicated values

Search, removal, and insertion : log(N)
*/

int main() {
    set<int> s = {1, 2, 3, 4, 5};

    s.insert(10);
    s.insert(10);
    s.insert(20);

    for (auto iter : s){
        cout << iter << " ";
    }
    cout << "\n";

    auto it = s.find(10);
    if (it != s.end())
        cout << *it << "\n";
    else
        cout << "no\n";

    it = s.find(50);
    if (it != s.end())
        cout << *it << "\n";
    else
        cout << "no\n";

    multiset<int> ms = {1,2,3};
    ms.insert(10);
    ms.insert(10);
    ms.insert(20);

    for (auto iter: ms){
        cout << iter << " ";
    }
    cout << "\n";

    cout << *ms.lower_bound(10) << "\n";
    cout << *ms.upper_bound(10) << "\n";

    return 0;
}