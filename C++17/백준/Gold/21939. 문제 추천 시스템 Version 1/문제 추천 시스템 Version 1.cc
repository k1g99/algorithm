#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int N, P, L, M; // 문제 개수, 문제 번호, 난이도, 명령어 개수
string cmd;
int X;
int prob[100001]; // 값이 1 이상 이면 관리 중인 문제 (문제 번호는 unique함)

priority_queue<pair<int, int> > hardProb;
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > easyProb;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int n = 0; n < N; n++){
        cin >> P >> L;
        hardProb.push(make_pair(L, P));
        easyProb.push(make_pair(L, P));
        prob[P] = L;
    }

    cin >> M;
    for (int m = 0; m < M; m++){
        cin >> cmd; 

        if( cmd == "add") {
            cin >> P >> L;
            hardProb.push(make_pair(L, P));
            easyProb.push(make_pair(L, P));
            prob[P] = L;
        }
        else if(cmd == "recommend"){
            cin >> X;
            if(X == 1){
                // {난이도, 문제번호}
                while(prob[hardProb.top().second] != hardProb.top().first){
                    hardProb.pop();
                }
                cout << hardProb.top().second << "\n";
            }else{
                while(prob[easyProb.top().second] != easyProb.top().first){
                    easyProb.pop();
                }
                cout << easyProb.top().second << "\n";
            }
        }else if(cmd == "solved"){
            cin >> X; // X = 문제번호
            prob[X] = 0;
        }
    }

    return 0;
}