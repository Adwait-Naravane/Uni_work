#include<stdio.h>  
int main(){   

int n,k,sum=0,tem;    
printf("Enter the number: ");    
scanf("%d",&n);    
tem = n;   

while(n>0){    
k = n%10;    
sum = (sum*10) + k;    
n = n/10;    
}   
 
if(tem==sum){    
printf("palindrome number ");}
else{    
printf("not palindrome");}

return 0;  
} 