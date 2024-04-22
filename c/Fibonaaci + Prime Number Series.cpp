#include<stdio.h>

bool check_prime(int p){
	if(p == 2){
		return true;
	}
	else{
		int i;
		for(i = 2; i <= (p/2); i++){
			if(p%i == 0){
				return false;
			}
		}
	}
	return true;
}

int main(){
	
	int a = 0, b = 1, ind, count = 1, pr = 2, temp;
	
	printf("Enter the index number of the series: ");
	scanf("%d",&ind);
	while(count<=ind){
		if(count%2 == 0){
			while(true){
				if(check_prime(pr)){
					printf("%d ", pr);
					pr++;
					break;
				}
				else{
					pr++;
				}
			}
			count++;
		}
		else{
			printf("%d ", b);
			temp = a + b;
			a = b;
			b = temp;
			count++;
		}	
	}
	
	return 0;
}
