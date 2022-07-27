#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;
string num2str[10] = {
	"zero","one","two","three","four","five","six","seven","eight","nine"
};

string num[10] = {
	"0","1","2","3","4","5","6","7","8","9"
};

int solution(string s) {

	int i;
	string tmp = s;

	for(i=0;i<tmp.length();i++){
		if(tmp[i] >= 'a' || tmp[i] <= 'z')
			break;
		else{
			return stol(tmp);
		}
	}

	for(i=0;i<10;i++){
		while(tmp.find(num2str[i]) != string::npos){
			tmp.replace(tmp.find(num2str[i]),num2str[i].length(),num[i]);
		}
	}

	long int answer = 0;

    return stol(tmp);
}

int main()
{
	char string[51];

	cin >> string;

	solution(string);

	return 0;
}
