#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <bitset>

using namespace std;
int number = 9;
int heap[9] = {1,2,3,4,5,6,7,8,9};

int main()
{
	int i,c,j;
	int temp;
	int root;

	//1. 힙 구조 생성
	for(i=1;i<number;i++){
		c = i;
		do{
			root = (c-1)/2;
			//root 가 자식보다 작으면 switch
			if(heap[root] < heap[c]){
				temp =  heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root;
		}while(c != 0);
	}

	printf("---------before sorting ----------\n");
	for(i=0;i<number;i++){
		printf("%d ",heap[i]);
	}
	printf("\n ");

	//2. 상위 root와 가장 하위 자식 바꿔가며 최대 힙 생성
	for(i=number-1 ; i >= 0; i--){
		//상위 root 랑 가장 마지막 자식 switch
		temp = heap[i];
		heap[i] = heap[0];
		heap[0] = temp;

		c = i;
		//상향식 heapify 실행
		//자식중에 더 큰 자식을 root와 비교해서 root보다 크면 switch
		do{
			root = (c-1)/2;
			//자식중에 더 큰 자식 찾기 정렬된 수랑 비교 안되게
			if(c < i-1 && heap[c] < heap[c-1])
				c--;

			if(c < i && heap[root] < heap[c]){
				temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c--;
		}while(c > 0);
	}

	printf("---------after sorting ----------\n");
	for(i=0;i<number;i++){
		printf("%d ",heap[i]);
	}
	printf("\n ");


	return 0;
}
