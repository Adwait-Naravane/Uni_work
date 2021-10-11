#include <stdio.h>

#define ROW 3
#define COL 3

void matrixInput(int mat[][COL]);
void matrixPrint(int mat[][COL]);
void matrixMultiply(int mat1[][COL], int mat2[][COL], int res[][COL]);

/*
I can't figure out how to check these two matrices without writing even larger codes 

*/

int main()
{
    int mat1[ROW][COL];
    int mat2[ROW][COL];
    int product[ROW][COL];


    
    printf("Enter elements in first matrix of size %dx%d\n", ROW, COL);
    matrixInput(mat1);


    matrixMultiply(mat1, mat1, product);

    printf("Product of both matrices is : \n");
    matrixPrint(product);

    if (areSame(mat1, product)){
        printf("Matrix is idempotent");
    }
    else{
        printf("MAtrix is not idempotent");
    }

    return 0;
}


void matrixInput(int mat[][COL])
{
    int row, col;

    for (row = 0; row < ROW; row++)
    {
        for (col = 0; col < COL; col++)
        {
            scanf("%d", (*(mat + row) + col));
        }
    }
}


void matrixPrint(int mat[][COL])
{
    int row, col;

    for (row = 0; row < ROW; row++)
    {
        for (col = 0; col < COL; col++)
        {
            printf("%d ", *(*(mat + row) + col));
        }

        printf("\n");
    }
}


void matrixMultiply(int mat1[][COL], int mat2[][COL], int res[][COL])
{
    int row, col, i;
    int sum;


    for (row = 0; row < ROW; row++)
    {
        for (col = 0; col < COL; col++)
        {
            sum = 0;

        
            for (i = 0; i < COL; i++)
            {
                sum += (*(*(mat1 + row) + i)) * (*(*(mat2 + i) + col));
            }

            *(*(res + row) + col) = sum;
        }
    }
}

int areSame(int A[][COL], int B[][COL])
{
    int i, j;
    for (i = 0; i < COL; i++)
        for (j = 0; j < COL; j++)
            if (A[i][j] != B[i][j])
                return 0;
    return 1;
}