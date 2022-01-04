#include <stdio.h>  

// swap elements in array
void swap(int *a, int *b) { 
int temp = *a; 
*a = *b; 
*b = temp; 
}   

//  Sorting algo
void Sort(int array[], int n) { 

int i, j, min_element; 
for (i = 0; i < n-1; i++) {

min_element = i; 

for (j = i+1; j < n; j++) 
if (array[j] < array[min_element]) 
min_element = j; 
swap(&array[min_element], &array[i]); 

} 
}   

void printarr(int array[], int size) { 
int i; 
for (i=0; i < size; i++){
printf("%d ", array[i]); 
}
 
}   
//  Function to execute all
int main() 
{ 
int arr[100]; 
int size; 
printf("Enter size of the array : ");
scanf("%d", &size);
printf("Enter elements in array : ");
for(int i=0; i<size; i++){
    scanf("%d ", &arr[i]);
}

Sort(arr, size); 
printf("Sorted array: \n"); 
printarr(arr, size); 
return 0; 
}
/*
* Just like q4, please run the program again after putting the input, 
* it doesn't seem to print the answer until it's run again.  (VScode atleast.)
*/