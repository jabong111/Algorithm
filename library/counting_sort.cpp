#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int number = 30;
int counting[30] = {1,3,2,4,3,2,5,3,1,2,3,4
	,4,3,5,1,2,3,5,2,3,1,4,3,5,1,2,1,1,1};

int main()
{
	int i,j;
	int cnt[5] = {0,};

	for(i=0;i<number;i++){
		cnt[counting[i] - 1] += 1;
	}

	for(i=0;i<5;i++){
		for(j=0;j<cnt[i];j++){
			printf("%d ",i+1);
		}
	}

	return 0;
}
