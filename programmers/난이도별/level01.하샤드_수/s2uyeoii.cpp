#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {

    int sum = 0;
    int x1 = x;

    while(x>=1)
    {
       sum += x1%10;
        x1/= 10;

        if(x1 == 0)
            break;

        }

    if (x % sum == 0)
    return  true;

    else
    return false;

}
