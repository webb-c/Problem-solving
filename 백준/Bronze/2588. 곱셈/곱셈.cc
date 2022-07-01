#include<stdio.h>
int main (void){
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    printf("%d\n",a*(b%10));
    printf("%d\n",a*(b%100/10));
    printf("%d\n",a*(b/100));
    printf("%d",a*(b%10)+a*(b%100/10)*10+a*(b/100)*100);
}