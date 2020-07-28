#include <iostream>
#include <string>

using namespace std;

string solution(string number, int k) {

	string answer = "";

		for (int j = 0, n = -1; j < number.length() - k; j++)
		{
		char max = 0;

		for (int i = n + 1; i <= j + k; i++) 
		{
			if (max < number[i]) {
				n= i;
				max = number[i];
			}

		}
		answer += max;
	}
	return answer;
}