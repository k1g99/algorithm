#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<char> wheel;
set<char> alpSet;
int wIdx = 0;
int N, K;
int rot;
char alp;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);


// INPUT
	cin >> N; // N
	cin >> K; // K
	
	// wheel은 처음에 ?로 초기회
	wheel.reserve(N);
	for (int n = 0; n < N; n++) {
		wheel.emplace_back('?');
	}


	// input 받으면서, 알파벳 추가하기
	// 단, 알파벳이 이미 있다면, 바로 ! 출력
	// [이거 놓침..ㅠ] 같은 알파벳은 2번 이상 등장하지 않는다!
	wIdx = 0;
	for (int k = 0; k < K; k++) {
		cin >> rot >> alp;

		wIdx += rot;
		wIdx %= N;

		// wIdx 자리가 ? 인 경우
		if (wheel[wIdx] == '?') {
			// 1) 값 넣기
			int bef = alpSet.size();
			wheel[wIdx] = alp;
			alpSet.insert(alp);

			// 2) 만약 동일한 알파벳이 이미 다른 자리에? -> !
			if (bef == alpSet.size()) { cout << '!' << endl; return 0; }
		}
		// wIdx 자리에 알파벳이 있는 경우
		else {
			// a) 같은 알파벳 -> continue;
			if (wheel[wIdx] == alp) { continue; }
			// b) 다른 알파벳 -> !
			else{ cout << '!' << endl; return 0; }
		}
	}

	


	// 출력
	for (int n = 0; n < N; n++) {
		cout << wheel[wIdx];

		wIdx -= 1;
		if(wIdx < 0) wIdx += N;
	}

	return 0;
}