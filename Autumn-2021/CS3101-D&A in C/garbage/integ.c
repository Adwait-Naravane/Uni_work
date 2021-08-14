#include <stdio.h>
#include <math.h>

double f(double x){
    return  pow(x,2);
}

double integ(double (*f)(double), double x0, double x1){
    const double delta = 1.0e-6;
    double sum = 0;
    for (int i = 1; i < (int) (x1-x0)/delta; ++i){
        sum += f(x0 + ((double) i)*delta);
    }
    return sum*delta; 
}

int main(){
    printf("%f", integ(f, 0.0, 1.0));
    return 0;
}