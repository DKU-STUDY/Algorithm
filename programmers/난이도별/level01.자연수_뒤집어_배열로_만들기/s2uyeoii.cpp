#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long num) {

	// num 최댓값 고려해 11자리 수
	int* answer = (int*)malloc(sizeof(int) * 11); 
  
	for (int i = 0; i < 11; i++) {
		answer[i] = num % 10;
		num /= 10;
	}

	return answer;
}
