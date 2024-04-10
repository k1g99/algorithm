#include <string>
#include <vector>
#include <iostream>

using namespace std;

int dp[10001];


int solution(int n) {
    if(n == 1) return 1;
    
    int answer = 0;
    
    int front = 1;
    int end = 1;
    int sum = 1;
    
    while (front <= n/2 && end <= n){
        if(sum == n){
            answer++;
            // std::cout << front << " " << end << "\n";

            sum -= front;
            front++;
        }else if (sum > n){
            sum -= front;
            front++;
        }else{
            end++;
            sum += end;
        }
    }
    
    return answer + 1;
}