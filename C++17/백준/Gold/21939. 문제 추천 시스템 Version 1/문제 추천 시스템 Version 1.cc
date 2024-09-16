#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int N, P, L, M; // 문제 개수, 문제 번호, 난이도, 명령어 개수
string cmd;
int X;
// multimap<int, int, greater<int> > prob; // key만 정렬이 되나봄...?

multiset<pair<int, int>, std::greater<pair<int, int> > > hardProb;
multiset<pair<int, int> > easyProb;
map<int, int> prob; // {문제번호, 난이도}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int n = 0; n < N; n++){
        cin >> P >> L;
        hardProb.insert(make_pair(L, P));
        easyProb.insert(make_pair(L, P));
        prob.insert(make_pair(P, L));
    }

    cin >> M;
    for (int m = 0; m < M; m++){
        cin >> cmd; 

        if( cmd == "add") {
            cin >> P >> L;
            hardProb.insert(make_pair(L, P));
            easyProb.insert(make_pair(L, P));
            prob.insert(make_pair(P, L));
        }
        else if(cmd == "recommend"){
            cin >> X;
            if(X == 1){
                cout << hardProb.begin()->second << "\n";
            }else{
                cout << easyProb.begin()->second << "\n";
            }
        }else if(cmd == "solved"){
            // prob에서 문제, 난이도 찾고 지우기
            cin >> X; // X = 문제번호
            pair<int, int> target = make_pair(prob[X], X);
            prob.erase(X);

            // 난이도Prob에서 난이도, 문제 찾고 지우기
            hardProb.erase(target);
            easyProb.erase(target);
        }
    }

    return 0;
}