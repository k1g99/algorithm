#include <iostream>
#include <string>
#include <set>
#include <unordered_set>

using namespace std;


unordered_set<string> unmap;
set<string> ans;
string s;
int N, M;

int main(){
    cin >> N >> M;
    
    for (int n = 0; n < N; n++){
        cin >> s;
        unmap.insert(s);
    }

    for (int m = 0; m < M; m++){
        cin >> s;
        if (unmap.find(s) != unmap.end()){
            ans.insert(s);
        }
    }

    cout << ans.size() << "\n";
    for (auto ss: ans){
        cout << ss << "\n";
    }

    return 0;
}