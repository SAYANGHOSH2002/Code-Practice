//Q. Find the maximum subarray from a 2D array of 0s and 1s. The sub array should contain only 1s.
//For example:
//	1 0 0 
//	0 1 1
//	1 1 1
//The maximum subarray is:
//	1 1
//	1 1

// Doing average of all counted elements approach. If the avg of all counted elements in the subarray is 1 then its taken 
// otherwise its not taken

#include<stdio.h>
#include<stdlib.h>

void printArray(int **arr2, int f, int m){
	
	for(int i = f; i < m; i++){
		for(int j = f; j < m; j ++){
			printf("%d ", arr2[i][j]);
		}
		printf("\n");
	}
	
}

void maxSubArray(int **arr1, int r){
	
	int c = 1, sum = 0, flag, max = -999;
	
	for(int i = 0; i < r; i++){
		for(int j = 0; j < r; j++){
			
			while((i + c) < r or (j + c) < r){
				
			 	for(int m = i; m <= (i + c); m++){
			 		for(int n = i; n <= (i + c); n ++){
			 			sum = sum + arr1[m][n];
					 }
				}
				 
				if(sum / (c*c) == 1){
					if(c > max){
						max = c;
						flag = i;
					}
					c++;
				}
			
			}
			
			c = 1;
			
		}
	}
	
	if(max == -999){
		printf("\nThe max sub array does not exist.");
	} else{
	printArray(arr1, flag, max);
	}
	
}

int main(){
	
	int rows, cols;
	
	printf("Enter the number of rows: ");
	scanf("%d",&rows);
	
	int **arr = (int **)malloc(rows * sizeof(int *));
	
	printf("\nStart entering values of the matrix, press enter to add new elements:\n");
	
	for(int i = 0; i < rows; i++){
		for(int j = 0; j < rows; j++){
			scanf("%d",&arr[i][j]);
		}
	}
	
	maxSubArray(arr, rows);
	
	return 0;
}
