#include <iostream>
#include <list>
#include <string>

using namespace std;

int N;
string input;
string ans;
list<char> pw;
list<char>::iterator cursor;

void pwMoveLeft(){
    if(cursor == pw.begin()){ cursor = pw.begin(); }
    else { cursor--; }
}

void pwMoveRight(){
    if(cursor == pw.end()){cursor = pw.end();}
    else {cursor++;}
}

void pwDel(){
    if(cursor != pw.begin()){
        cursor = pw.erase(--cursor);
    }
}

void pwInsert(char word){
    pw.insert(cursor, word);
}

void solve(){
    ans = "";
    pw.clear();
    cursor = pw.end();
    // 특수문자 :  <, >, -

    for (auto word : input){
       if(word == '<'){pwMoveLeft();} 
       else if(word == '>'){pwMoveRight();} 
       else if(word == '-'){pwDel();} 
       else {pwInsert(word);}
    }

    for (auto word: pw){
        cout << word;
    }
    cout << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

// INPUT
    cin >> N;

    for (int n = 0; n < N; n++){
        cin >> input;
        solve();
    }

    return 0;
}