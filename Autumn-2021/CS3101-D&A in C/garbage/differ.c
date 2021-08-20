#include <stdio.h>
#include <math.h>

double f(double x){
   return pow(x,2) + 3*x;
}
double derive(double (*f)(double), double x0){
   const double delta = 1.0e-6;
    double x1 = x0 - delta;
    double x2 = x0 + delta;
    double y1 = f(x1);
    double y2 = f(x2);
   return (y2-y1)/(x2-x1);
}
int main(){
   double der = derive(f, 1.0); 
   printf("%f",der);
   return 0;
}