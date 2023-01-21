#include <iostream>

int main() {
    long long n;
    std::cin >> n;
    if (n==1)
        std::cout << 0;
    else
        std::cout << (n+1)/2;
    return 0;
}