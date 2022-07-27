#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int solution(vector<int> numbers) {

	int i;
	int answer = 0;
	int check = 0;
	int cnt = 0;
	sort(numbers.begin(), numbers.end());

	for(i=0;i<=9;i++){
		cnt = 0;
		check = 0;
		while(cnt < numbers.size()){
			if(numbers[cnt] == i){
				check = 1;
				break;
			}
			cnt++;
		}

		if(!check){
			answer += i;
		}
	}

	cout << answer << endl;
	
	return answer;

}

int main()
{
	int i,n;
	cin >> n;
	vector<int> numbers(n);

	for(i=0;i<n;i++){
		cin >> numbers[i];
	}

	solution(numbers);
	

	return 0;
}
