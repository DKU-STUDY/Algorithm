#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// prices_len은 배열 prices의 길이입니다.
int* solution(int prices[], size_t prices_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(prices_len*sizeof(int));
    int i,j;
    for(i=0;i<prices_len;i++){
        answer[i] = 0;
        j = i+1;
        while(j<prices_len){
            if(prices[i]<=prices[j]){
                answer[i]++;
                j++;
            }
            else{
                answer[i]++;
                break;
            }
        }
    }
    return answer;
}
