#include<stdio.h>
#include<stdlib.h>


void selectionSort(int *ar, int n){
	
	int c;
	for(int i = 0; i < n; i++){
		int minEle = ar[i];
		c = i;
		for(int j = i; j < n; j++){
			if(ar[j] <= minEle){
				minEle = ar[j];
				c = j;
			}
		}
		int temp = ar[c];
		ar[c] = ar[i];
		ar[i] = temp;
	}
	
}

int main(){
	int n;
	
	printf("Enter the number of elements: ");
	scanf("%d",&n);
	
	int *arr = (int*)malloc(n*(sizeof(int)));
	
	printf("Enter the elements: \n");
	
	for(int i = 0; i < n; i++){
		scanf("%d",&arr[i]);
	}
	
	printf("\nInitial Array: ");
	for(int i = 0; i < n; i++){
		printf("%d ", arr[i]);
	}
	printf("\nSorted Array: ");
	selectionSort(arr, n);
	
	for(int i = 0; i < n; i++){
		printf("%d ", arr[i]);
	}
	
	return 0;
	
}
