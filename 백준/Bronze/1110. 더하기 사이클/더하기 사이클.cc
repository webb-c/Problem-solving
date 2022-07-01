#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    int num = 0;
    int snum = 0;
    int n = 0;
    int i = 0;
    scanf("%d", &num);
    snum = num;

    while (true) {
        n = num / 10 + num % 10;
        num = (num % 10) * 10 + n % 10;
        i++;
        if (num == snum) break;
    }

    printf("%d", i);
    return 0;
}