#include <iostream>

using namespace std;
char arr[6562][6562];

void dac(int start_y, int end_y, int start_x, int end_x)
{
	int q = (end_y - start_y + 1) / 3;
	if (q != 1)
	{
		for (int i = start_y; i < end_y; i += q) for (int j = start_x; j < end_x; j += q)
		{
			dac(i, i + q - 1, j, j + q - 1);
		}
		for (int i = start_y + q; i < start_y + q + q; i++) for (int j = start_x + q; j < start_x + q + q; j++)
		{
			arr[i][j] = ' ';
		}
	}
	else
	{
		for (int i = start_y; i <= end_y; i++)for (int j = start_x; j <= end_x; j++)
			arr[i][j] = '*';
		arr[(start_y + end_y) / 2][(start_x + end_x) / 2] = ' ';
	}
}

int main()
{
	int N;
	cin >> N;
	dac(1, N, 1, N);
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
			printf("%c", arr[i][j]);
		printf("\n");
	}

}