#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int w, int h) {

	/*사용할 수 있는 정사각형의 개수가 들어가는 변수, 'w', 'h'는 1억 이하의 자연수이므로 두 매개변수의 곱은 int형을 넘어가기에 long long형으로 설정*/

	long long answer = 0;
	// 각 열마다 잘린 부분 전까지 사용할 수 있는 정사각형의 개수를 담는 변수
	long long block = 0;

	// 대각선으로 잘릴 경우, 동일한 정사각형의 개수를 가지는 직각삼각형이 두개 만들어진다
	// 이를 기울기 * 행의 좌표(w*i / h)를 통해 'block'을 구하여
	// 직각삼각형에 들어가는 정사각형 수를 구하고 2배를 해주면서 'answer'을 구하는 동작
	for (int i = 0; i < h; i++) {
		block = (long long)w*i / h;
		answer += (2 * block);
	}

	return answer;
}