#include <stdio.h>
#include <iostream>

using namespace std;
int s, k, n[10];
int main() {
	while (~scanf("%1d", &k))
		n[k]++, s += k;
	if (s % 3 || !n[0])
		printf("-1");
	else
		for (int i = 9; i >= 0; i--)
			while (n[i]--)
				printf("%d", i);
}