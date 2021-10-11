#include<stdio.h>

int main(int argc, char const *argv[]){
    int n;
    printf("Enter Number of levels : ");
    scanf("%d",&n);
    int c = 1;
    for (int i = 1; i < n; i++){     
        for (int j = (n); j > i; j--){
            printf(" ");
        }
        for (int k = 1; k < i+1; k++){
            if (c == 1){
                printf("%d ",k);
            }
            else if (c == 3){
                printf("%d ",k);
            }
            else{
                printf("0 ");
            }
            c ++;
            if (c > 6){
                c = 1;
            }
                
        }
        c=1;
        printf("\n");
    }
    
    return 0;
}
