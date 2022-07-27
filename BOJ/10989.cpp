#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
	int n,i,j,tmp;
	int cnt[10000] = {0,};

	cin >> n;

	for(i=0;i<n;i++){
		scanf("%d",&tmp);
		if(tmp != 0){
			cnt[tmp - 1] += 1;
		}
	}

	for(i=0;i<10000;i++){
		for(j=0;j<cnt[i];j++){
			printf("%d\n",i+1);
		}
	}



	return 0;
}
