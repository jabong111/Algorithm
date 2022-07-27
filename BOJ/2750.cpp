#include <iostream>
#include <algorithm>
#include <string>
#include <bitset>

using namespace std;

int data[1000] = {0,};

void quick_sort(int* data, int start/*pivot*/, int end)
{
	int i, j, temp,pivot;

	if(start >= end)
		return;

	pivot = start;
	i = start + 1;
	j = end;

	while(i <= j){

		while(data[i] <=  data[pivot]){
			i++;
		}

		while(data[j] >= data[pivot] && j > start){
			j--;
		}

		if(i > j){
			temp = data[pivot];
			data[pivot] = data[j];
			data[j] = temp;
		}else{
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
		}
	}

	 quick_sort(data, start, j-1);
	 quick_sort(data, j+1, end);

}

int main()
{
	int i,number,input;

	scanf("%d",&number);

	for(i = 0;i<number;i++){
		scanf("%d",&input);
		data[i] = input;
	}

	quick_sort(data, 0, number-1);

	for(i=0;i<number;i++){
		printf("%d\n",data[i]);
	}



	return 0;
}
