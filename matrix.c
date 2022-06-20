#include<stdio.h>
int gcd(int a,int b); 
int main()
{
int a,b;
int r,t;
    printf("Enter any two integers");
    scanf("%d %d",&a,&b);
    r=gcd(a,b);
    printf("GCD=%d",r); 
    return 0;
}
int gcd(int a,int b)
{
int t,rem;
while (1)
{
    if(b>a)
    {
        t=a;
        a=b;
        b=t;
    }
if(b==0)
return a;

else
{
        rem=a%b; 
        a=rem;
        }
    }
}