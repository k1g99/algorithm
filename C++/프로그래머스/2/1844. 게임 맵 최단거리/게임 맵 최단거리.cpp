#include <vector>
#include <queue>
#include <iostream>
using namespace std;

bool check_bound(pair<int, int> cell, int hh, int ww){
    int r = cell.first;
    int c = cell.second;
    
    return r>=0 && c>=0 && r<hh && c<ww;
}

int solution(vector<vector<int>> maps){
    int answer = 0;
    int dir[4][2] = {{-1,0}, {1,0}, {0,1}, {0,-1}};
    int wid = 0;
    int hei = 0;
    int visited[101][101] = {0};
    
    hei = maps.size();
    wid = maps[0].size();
    
    queue<pair<int, int>> que;
    que.emplace(make_pair(0,0));
    visited[0][0] = 1;
    
    while(!que.empty()){
        auto curr = que.front(); que.pop();
        for (int d = 0; d < 4; d++){
            auto nxt = make_pair(curr.first + dir[d][0], curr.second + dir[d][1]);
            if(check_bound(nxt, hei, wid) && maps[nxt.first][nxt.second] == 1
               && visited[nxt.first][nxt.second] == 0){
                visited[nxt.first][nxt.second] = visited[curr.first][curr.second] + 1;
                que.emplace(nxt);
            }
        }
    }
    
    
    answer = visited[hei-1][wid-1];
    if(answer == 0) answer = -1;
    
    
    return answer;
}