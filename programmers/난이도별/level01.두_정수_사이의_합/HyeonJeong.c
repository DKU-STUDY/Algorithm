#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long answer = 0;

    if(a>b)
        for(int i = 0; i <= a - b; i++)
            answer += b + i;
    else if(a<b)
        for(int i = 0; i <= b - a; i++)
            answer += a + i;
    else
        answer = a;
    return answer;
}
