#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int way_cnt[4][3];
int checked[4][3];
char keypad[4][3] = {
	{'1','2','3'},
	{'4','5','6'},
	{'7','8','9'},
	{'*','0','#'}
};

/*
    0 1 2
   ----------
0  |1 2 3
1  |4 5 6
2  |7 8 9
3  |* 0 #
 */

void default_map_set(void)
{
	int i;
	for(i=0;i<4;i++){
		memset(way_cnt[i],0,sizeof(int)*3);
		memset(checked[i],0,sizeof(int)*3);
	}
}

void dfs(pair<int,int> pos, int goal)
{
	int x,y;
	int mvx,mvy;
	int i,j;
	x = pos.first;
	y = pos.second;

	if(checked[x][y])
		return;

	checked[x][y] = 1;

	for(i = 0; i<4; i++){
		mvx = x + dx[i];
		mvy = y + dy[i];
		if((0 <= mvx  && mvx <4) && (0 <= mvy && mvy < 3)){
			if((keypad[mvx][mvy] == '2' || keypad[mvx][mvy] == '5' || keypad[mvx][mvy] == '8' ||	keypad[mvx][mvy] == '0') && !checked[mvx][mvy]){
				way_cnt[mvx][mvy] = way_cnt[x][y] + 1;
				if(keypad[mvx][mvy] == goal + '0'){
					return;
				}
				dfs(make_pair(mvx,mvy),goal);
			}
		}
	}
}

pair<int,int> find_position(int number)
{
	int i,j;
	int find_num = number + '0';

	for(i=0; i<4; i++){
		for(j=0; j<3; j++){
			if(keypad[i][j] == find_num){
				return make_pair(i,j);
			}
		}
	}

	return make_pair(0,0);
}


string solution(vector<int> numbers, string hand)
{
	int i;
	int right_cnt = 0;
	int left_cnt = 0;
	pair<int,int>	left_hand_pos = make_pair(3,0);
	pair<int,int>	right_hand_pos = make_pair(3,2);
	pair<int,int>	curr_position; string answer = "";

	for(i=0;i<numbers.size();i++){
		curr_position = find_position(numbers[i]);
		default_map_set();
		//1,4,7이면 왼속으로 바로 움직이고 position을 옮겨준다.
		if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7){
			left_hand_pos = curr_position;
			answer += "L";
			continue;
		}else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9){
			right_hand_pos = curr_position;
			answer += "R";
			continue;
		}

		//2,5,8,0 이면 왼손으로 움직인 거리계산
		dfs(right_hand_pos, numbers[i]);
		right_cnt = way_cnt[curr_position.first][curr_position.second];
		default_map_set();

		//2,5,8,0 이면 오른손으로 움직인 거리계산
		dfs(left_hand_pos, numbers[i]);
		left_cnt = way_cnt[curr_position.first][curr_position.second] ;

		if(right_cnt > left_cnt){
			left_hand_pos = curr_position;
			answer += "L";
		}else if(right_cnt < left_cnt){
			right_hand_pos = curr_position;
			answer += "R";
		}else{
			if(hand == "right"){
				right_hand_pos = curr_position;
				answer += "R";
			}else if(hand == "left"){
				left_hand_pos = curr_position;
				answer += "L";
			}
		}
	}

	cout << answer << endl;

    return answer;
}

int main()
{
	string hand;
	int number;
	int i;

	cin >> number;
	vector<int> input(number);

	for(i=0;i<number;i++){
		cin >> input[i]; 
	}

	cin >> hand;

	solution(input, hand);

	return 0;
}
