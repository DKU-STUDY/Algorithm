#include <iostream>

using namespace std;

int main()
{
	int N, M;
	cin >> N >> M;
	int* A = new int[N];
	int* B = new int[M];
	int* C = new int[N + M];

	for (int i = 0; i < N; i++)
		scanf("%d", &A[i]);
	for (int i = 0; i < M; i++)
		scanf("%d", &B[i]);
	int a = 0, b = 0, c = 0;
	while (a < N && b < M)
		if (A[a] >= B[b])
			C[c++] = B[b++];
		else
			C[c++] = A[a++];

	while (a < N)
		C[c++] = A[a++];

	while (b < M)
		C[c++] = B[b++];

	for (int i = 0; i < N + M; i++)
		printf("%d ", C[i]);
}