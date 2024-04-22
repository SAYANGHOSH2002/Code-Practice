//The square root of a Prime number by checking first if it is a prime number? 
//Write a C program which will check whether a given number N is a Prime or Not. 
//If the Number N is a Prime, then find it’s square root and print that value to the STDOUT as floating point number with exactly 2 decimal precision. 
//If the number is not Prime, then print the value 0.00 to STDOUT. 
//The given number will be positive non zero integer and it will be passed to the program as first command line argument. 
//Other than floating point No other information should be printed to STDOUT.

#include<stdio.h>
#include<math.h>

bool check_prime(int a){
	
	for(int i = 2; i <= int(a/2); i++){
		if (a%i == 0)
			return false;
	}
	return true;
}

int main(){
	int num;
	
	printf("Enter the number: ");
	scanf("%d",&num);
	
	if (check_prime(num)){
		float s = sqrt(num);
		printf("\n%.2f", s);
	}
	else{
		printf("\n0.00");
	}
	
	return 0;
}
