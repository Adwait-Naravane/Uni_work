/*
* SHIVAM KUMAR
* 19MS123
* CS3101 Q1
*/

#include<stdio.h>
#include<string.h>

int main(){
    int nos[3];
    int min;
    for(int i = 0; i <3; i++){
        printf("Enter a number %d: ", i+1);
        scanf("%d", &nos[i]);
    }
    min = nos[0];
    for(int j = 0; j<3; j++){
        min = (min<nos[j])?min:nos[j];
    }
    printf("\nsmaller number = %d", min);
    return 0;
}