#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    
    int answer_length = number.length() - k;
    int answer_len = number.length() - k;
// 01234 56789
// 41772 52841
    
    int start = 0;
    int end = number.length() - answer_len + 1;
    while(answer.length() < answer_length){
        int max_num = -1;
        int max_idx = -1;
        for (int i = start; i < end; i++){
            if(max_num < int(number[i])){
                max_num = int(number[i]);
                max_idx = i;
            }
        }
        number.erase(max_idx, 1);
        start = max_idx;
        answer_len--;
        end = number.length() - answer_len + 1;
        answer.push_back(char(max_num));
    }
    
    return answer;
}


