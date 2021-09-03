#include<stdio.h>
#include<string.h>

int main(){
    int a,b,c;
    printf("Enter 3 subject marks: " );
    scanf("%d %d %d",&a, &b ,&c);
    int sum = a + b + c;   
    int rem = sum % 5;
    switch (rem)
    {
    case 0: printf("Pentagon");
        break;
    case 1: printf("Unicorn");
        break;
    case 2: printf("Double Deluda");
        break;
    case 3: printf("Three idiots");
        break;
    case 4: printf("Sign of four");
        break;
    
    default:
        printf("Invalid!");
    }

    return 0;

}