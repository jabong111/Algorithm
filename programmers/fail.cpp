#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

/*
   1. 1~N 스테이지를 돈다.
   2. 현재 스테이지보다 높거나 같은 사람들은 현재 스테이지를 시도했던 사람들이므로
      시도한 사람 cnt를 증가시키고, 현재 스테이지에 머물러있는 사람을 cnt한다.
   3. 머물러있는 사람 / 시도했던 사람들 로 실패율을 구한다.
   4. 1~N 배열에 실패율 저장
*/

bool compare(pair<int, float> a, pair<int, float> b)
{
	if(a.second == b.second){
		return a.first < b.first;
	}else{
		return a.second > b.second;
	}
}


vector<int> solution(int N, vector<int> stages) {

	vector<int> answer(N);
	vector< pair<int, float> > fail(N);
	int i,j;
	float try_cnt = 0;
	float loser_cnt = 0;
	float fail_rate;

	for(i=1;i<=N;i++){
		
		loser_cnt = count(stages.begin(), stages.end(),i);
		if(loser_cnt == 0){
			fail[i-1] = make_pair(i,0);
			continue;
		}

		try_cnt = 0;
		for(j = 0; j < stages.size();j++){
			if( i <= stages[j]){
				try_cnt++;
			}
		}

		fail_rate = loser_cnt / try_cnt;
//		printf(" %f %f   %lf \n" , loser_cnt, try_cnt, fail_rate);
		fail[i-1] = make_pair(i ,fail_rate);
	}

	sort(fail.begin(), fail.end(), compare);
	for(i=1;i<=N;i++){
	//	cout << fail[i-1].first<< endl;
		answer[i-1] = fail[i-1].first;
//		cout << answer[i-1] << " ";
	}
//	cout << endl;

	return answer;
}

int main()
{
	int n,i,stage_n;
	vector<int> stages(200000);
	cin >> n;

	cin >> stage_n;

	for(i=0;i<stage_n;i++){
		cin >> stages[i];
	}

	solution(n,stages);


	return 0;
}
