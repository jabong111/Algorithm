#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums)
{
	vector<int> ans(2);
	int answer = 6;
	int zero_cnt = 0;
	int i;

	for(i=0;i<6;i++){
		if(lottos[i] == 0){
			zero_cnt++;
			continue;
		}

		auto it = find(win_nums.begin(), win_nums.end(),lottos[i]);
		if(it != win_nums.end()){
			answer--;
		}

	}

	ans[0] = answer - zero_cnt;
	ans[1] = answer;

	for(i=0;i<2;i++){
		switch(ans[i]){
			case 0:
				ans[i] = 1;
				break;
			case 1:
				ans[i] = 2;
				break;
			case 2:
				ans[i] = 3;
				break;
			case 3:
				ans[i] = 4;
				break;
			case 4:
				ans[i] = 5;
				break;
			default:
				ans[i] = 6;
				break;
		}
	}

	cout << ans[0] << " " << ans[1] << endl;


	return ans;
}

int main()
{
	int i;
	vector<int> lottos(6);
	vector<int> win_nums(6);

	for(i=0;i<6;i++){
		cin >> lottos[i];
	}

	for(i=0;i<6;i++){
		cin >> win_nums[i];
	}

	solution(lottos, win_nums);


	return 0;
}
