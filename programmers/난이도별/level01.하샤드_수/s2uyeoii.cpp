#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {

    int sum = 0;
    int x1 = x;

    while(x>=1 || x1 != 0)
    {
       sum += x1 % 10;
        x1 /= 10;
    }

    return x % sum == 0;

}
