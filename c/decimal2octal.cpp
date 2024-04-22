//Basic Program for Decimal to Octal Given a decimal number as input, we need to write a program to convert the given decimal number into equivalent octal number. 
//i.e convert the number with base value 10 to base value 8. The base value of a number system determines the number of digits used to represent a numeric value. 
//For example, the binary number system uses two digits 0 and 1, octal number system uses 8 digits from 0-7 and decimal number system uses 10 digits 0-9 to represent any numeric value. 
//Examples: Input : 16 Output : 20 Input : 10 Output : 12

#include<stdio.h>
#include<math.h>

int decimal2Octal(int n){

	int a, i = 0, sum = 0;
	
	while(n > 0){
		a = n % 8;
		n = n / 8;
		sum = sum + a*pow(10, i);
		i++;	
	}
	return sum;
}

int main(){
	
	int num;
	
	printf("Enter the decimal number: ");
	scanf("%d",&num);
	
	printf("\nThe equivalent octal number is: %d", decimal2Octal(num));
	
	return 0;
}
