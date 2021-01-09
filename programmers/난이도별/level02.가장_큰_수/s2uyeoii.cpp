#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//주어진 원소 숫자 비교
int str_compare(int* num1, int* num2) {
    char num_cmp1[10] = ""; //0~10까지 
    char num_cmp2[10] = "";

    sprintf(num_cmp1, "%d%d", *num1, *num2); //주어진 문자 문자열 저장
    sprintf(num_cmp2, "%d%d", *num2, *num1);

    if (strcmp(num_cmp1, num_cmp2) < 0) return 1; 
    if (strcmp(num_cmp1, num_cmp2) == 0) return 0;
    return -1;
}

// numbers_len은 배열 numbers의 길이입니다.
char* solution(int numbers[], size_t numbers_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char nums[5] = "";
    int len = 0;
    bool isZeroCheck = false;

    qsort(numbers, numbers_len, sizeof(int), str_compare); //위 비교함수대로 정렬

    for (int i=0; i<numbers_len; i++) {
        len += sprintf(nums, "%d", numbers[i]);
    }
    char* answer = (char*)malloc(len+1);
    memset(answer, '\0', len+1);

    for (int i=0; i<numbers_len; i++) {
        sprintf(nums, "%d", numbers[i]);
        strcat(answer, nums);
    }

    for (int i=0; i<len; i++) {
        if (answer[i] != '0') {
            break;
        } else {
            isZeroCheck = true;
        }
    }

    if (isZeroCheck) {
        isZeroCheck = false;
        return "0";
    }

    return answer;
}
