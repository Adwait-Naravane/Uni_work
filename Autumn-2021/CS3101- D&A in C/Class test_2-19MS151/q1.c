#include<stdio.h>
#include<string.h>

int main(){
    int a,b,c;
    int min;
    printf("Enter 3 numbers: ");
    scanf("%d %d %d",&a, &b, &c);
    int num[3] = {a, b, c};
    
    min = num[0];
    for(int j = 0; j<3; j++){
        min = (min<num[j])?min:num[j];
    }
    printf("\nsmallest  number = %d", min);
    return 0;
}