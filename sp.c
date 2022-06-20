#include<stdio.h>
void main()
{
    int p;
    float a;
    double s,u;
    printf("cost price : ");
    scanf("%f", &a);
    printf("profit percent : ");
    scanf("%d", &p);
    u=p+100/100;
    s=u*a;
    s=s/10;
    printf("selling price :%lf\n",s);
}