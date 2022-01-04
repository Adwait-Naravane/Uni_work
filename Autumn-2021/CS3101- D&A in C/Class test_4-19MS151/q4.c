#include <stdio.h>

int main(){
    char names[20][20];
    // forgot what we use in place of int for decimals. 
    float judge1[100], judge2[100], judge3[100];
    float marks[100];
    int size;
    printf("Enter total number of contestants  : ");
    scanf("%d", &size);
    printf("\n Enter the names: ");
    for (int i = 0 ;  i < size; i++){
        scanf("%s", &names[i]);
    }
    
    /*
    Add rank in order of names, like if first person got rank 2, second got rank 1 , so on then input {2, 1 ..}. 
    */

    printf("\n Judge1, please enter your rankings: ");
    for (int i = 0; i<size; i++){
        scanf("%f", &judge1[i]);
    }
    printf("\n Judge2, please enter your rankings: ");
    for (int i = 0; i<size; i++){
        scanf("%f", &judge2[i]);
    }
    printf("\n Judge3, please enter your rankings: ");
    for (int i = 0; i<size; i++){
        scanf("%f", &judge3[i]);
    }

    for (int i = 0; i <size; i++){
        marks[i] = 1/judge1[i] + 1/judge2[i] + 1/judge3[i];
    }

    for (int k = 0; k <size; k++){
        printf("%s got %f marks, \n", names[k], marks[k]);
    }
    
/*
This "works", but really bad code.
*/

return 0;
}