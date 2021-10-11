#include <stdio.h>
#include <math.h>

int fac(int n)
{
    int i,f=1;
    for(i=1;i<=n;i++)
    {
        f=f*i;
    }
    return f;
}

float series(float x, int n)
{
   

    if (n != 1){
        return series(x, n-1) + pow(-1, n+1) * pow(x, 2*n - 1) / fac(2*n -1 );
    }
    else{
        return x;
    }
}
int main ()
{
  int n = 2;
  float x = 2.0;
  printf("%f", series(x, n));
  
  return 0;
}