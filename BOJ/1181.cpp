#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

bool compare(string a, string b)
{
	
	if(a.length() == b.length()){
		return  a < b;
	}else{
		return  a.length() < b.length();
	}
}

int main()
{
	int n,i;
	string str[20000];

	cin >> n;

	for(i=0;i<n;i++){
		cin >> str[i];
	}
	sort(str, str+n,compare);

	for(i=0;i<n;i++){
		if(str[i] == str[i+1] && i+1 < n)
			continue;
		cout << str[i]<< "\n";
	}


	return 0;
}
