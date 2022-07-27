#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

string str[50];

int sum_of_str2num(string a)
{
	int i;
	int sum = 0;
	int str2int;
	for(i=0; i< a.length(); i++){
		str2int = a[i] - '0';
		if(0 <= str2int && str2int <= 9) {
			sum += str2int;
		}
	}
	return sum;
}

bool compare(string a, string b)
{
	int a_number;
	int b_number;

	if(a.length() != b.length()){
		return a.length() < b.length();
	}else{
		a_number = sum_of_str2num(a);
		b_number = sum_of_str2num(b);

		if(a_number != b_number){
			return a_number < b_number;
		}else{
			return a < b;
		}
	}
}

int main()
{
	int i;
	int number;
	int zero = '0';
	int nine = '9';

	cin >> number;

	for(i=0;i<number;i++){
		cin >> str[i];
	}
	sort(str,str+number,compare);

//	cout <<  sum_of_str2num(str[0]) << "\n";

	for(i=0;i<number;i++){
		cout << str[i] << "\n";
	}

	return 0;
}
