#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

string solution(string new_id) {
	int i;
	int cnt = 0;
	char tmp[1001] = {0,};
	char origin[1001] = {0,};

   //1. 소문자로 변경 
	for(i=0;i<new_id.length();i++){
		if(new_id[i] >= 'A' && new_id[i] <= 'Z'){
			new_id[i] = new_id[i] + ('a'-'A');
		}
	}

	//2. alphabet, number, -,_,. 이외는 모두 제거
	for(i=0;i<new_id.length();i++){
		if((new_id[i] >= 'a' && new_id[i] <= 'z') ||
			(new_id[i] >= '0' && new_id[i] <= '9') ||
			new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.'){
			tmp[cnt] = new_id[i];
			cnt++;
		}
	}

	string str1(tmp);
	new_id = tmp;

	memset(tmp, 0, sizeof(tmp));

	//3. 연속된 . 제거
	cnt = 0;
	i = 0;
	while(i < new_id.length()){
		if(new_id[i] == '.'){
			tmp[cnt++] = new_id[i];
			while(new_id[i] == '.'){
				i++;
			}
		}
		tmp[cnt++] = new_id[i];
		i++;
	}

	string str2(tmp);
	new_id = tmp;
	memset(tmp, 0, sizeof(tmp));

	//4. 처음이나 마지막에 .이 있으면 제거
	cnt = 0;
	for(i=0;i<new_id.length();i++){
		if(i == 0 && new_id[0] == '.'){
			continue;
		}

		if(i == new_id.length()-1 && new_id[new_id.length()-1] == '.'){
			continue;
		}
		tmp[cnt++] = new_id[i];
	}

	string str3(tmp);
	new_id = tmp;

	memset(tmp, 0, sizeof(tmp));


	//5. new_id 가 빈문자열이라면, new_id에 'a'를 대입한다.
	if(new_id.empty()){
		new_id.append("a");
		memset(tmp, 0, sizeof(tmp));
	}


	//6. new_id 가 16자 이상이면 15자만 남김 , 제거 후 마지막에 . 이 남아있으면 제거
	cnt = 0;
	if(new_id.length() >= 16){
		for(i=0;i<=14;i++){
			if(i == 14 && new_id[i] == '.'){
				break;
			}
			tmp[cnt++] = new_id[i];
		}

		string str4(tmp);
		new_id = tmp;

		memset(tmp,0,sizeof(tmp));
	}

	//7. 

	if(new_id.length() <= 2){
		while(new_id.length() != 3){
			new_id += new_id[new_id.length()-1];
		}
	}

	cout << new_id << endl;


    string answer = "";
    return answer;
}

int main()
{
	string str;
	cin >> str;
	solution(str);


	return 0;
}
