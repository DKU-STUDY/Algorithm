#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(void){
    printf("%d %d", &solution(a,b), 12L)
}

long long solution(int a, int b) {
    long long answer = 0;

    if(a != b){
        int max = a > b ? a : b;
        int min = a < b ? b : a;

        for (int i = 0; i <= max - min; i++)
        answer += min + i;
    }
    else
        // a와 b가 같은 경우는 둘 중 아무 수나 리턴
        answer = a;

    return answer;
}