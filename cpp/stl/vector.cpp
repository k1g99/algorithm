#include <iostream>
#include <vector>

using namespace std;

/*
emplace_back VS push_back
    - push_back : 2 steps 
	    1. The new element is initialized as a copy of value.
	    2. value is moved into the new element.
    - emplace_back : forwards parameters without copy or move operation 

vector VS array
    - vector : dynamic array  / access elements with `iterator`
    - array : static array ( fixed size )
*/

int main() {
    vector<int> vec = {1,2,3};

    vec.emplace_back(4);
    vec.emplace_back(5);

    for (vector<int>::iterator iter = vec.begin(); iter != vec.end(); ++iter){
        cout << *iter << " ";
    }
    cout << endl;
    cout << vec.back() << endl;
    
    vec.pop_back();
    
    for (vector<int>::iterator iter = vec.begin(); iter != vec.end(); ++iter){
        cout << *iter << " ";
    }
    cout << endl;

    cout << vec[3] << "\n"; 

    return 0;
}