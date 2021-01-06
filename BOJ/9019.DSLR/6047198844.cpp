#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

string BFS(int A, int B)
{
    bool check[10000]; // 전역일때는 all false, 지역일때는 all true;
    fill_n(&check[0], 10000, false);
    queue <pair<int, string>> q;
    int target = B;
    string res_string = "";
    q.push(make_pair(A, res_string)); check[A] = true;
    while (!q.empty())
    {
        int size = q.size();
        for (int i = 0; i < size; i++)
        {
            int num = q.front().first; string bfs_string = q.front().second;
            q.pop();
            int check_num[4] = { (2 * num) % 10000,(num - 1) < 0 ? 9999 : num - 1,(num % 1000) * 10 + (num / 1000),(num / 10) + (num % 10) * 1000 };
            string commend_string[4] = { "D","S","L","R" };

            for (int i = 0; i < 4; i++)
            {
                if (num == target)
                    return bfs_string;
                if (!check[check_num[i]])
                {
                    check[check_num[i]] = true;
                    q.push(make_pair(check_num[i], bfs_string + commend_string[i]));
                }
            }
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        int A, B;
        cin >> A;
        cin >> B;
        cout << BFS(A, B) << "\n";
    }
}