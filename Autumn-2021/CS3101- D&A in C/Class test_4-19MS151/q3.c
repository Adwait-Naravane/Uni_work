#include <stdio.h>

int main(){
    int arr[100];
    int i, j, size, count = 0;
    int dup[100];
    int index = 0;
    /* Input size of array */
    printf("Enter size of the array : ");
    scanf("%d", &size);

    /* Input elements in array */
    printf("Enter elements in array : ");
    for(i=0; i<size; i++)
    {
        scanf("%d ", &arr[i]);
    }

    /*
     * Find all duplicate elements in array
     * Also append to a list of duplicates  
     */
    for(i=0; i<size; i++)
    {
        for(j=i+1; j<size; j++)
        {
            /* If duplicate found then increment count by 1 */
            if(arr[i] == arr[j])
            {
                count++;
                dup[index++] = arr[j];
                break;
            }
        }
    }
    
    /*
    Please run the program again after giving input, coz it doesnt show anything the first time..
    */

    printf("\nTotal number of duplicate elements found in array = %d", count);
    printf("\n");
    for (int k = 0; k < count; k++){
        printf("%d ", dup[k]);
    }

    return 0;
}