1
/*
2
이분그래프
3
- 그래프의 정점을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할 할수있는 그래프
4
- 그리프가 입력으로 주어졌을때, 이분 그래프인지 아닌지 판별하라.
5
​
6
풀이
7
- 인접한 그래프들 원소 각각에 색깔을 칠한다 -> 칠한 색깔이 맞는지 검증한다.
8
​
9
- n개의 조각으로 쪼갠다.
10
   - 모든 그래프에 색을 칠한다.
11
   - 그래프 탐색을 한다. 근처 원소에 색을 칠해야 하므로 BFS로 색을 칠한다.
12
​
13
- Base case
14
   - 모든 원소가 색이 칠해졌을때
15
​
16
검증하는 함수 작성
17
- 빨강은 1 / 검정은 2로 표시한다.
18
*/
19
​
20
#include <iostream>
21
#include <queue>
22
#include <string.h>
23
#include <vector>
24
​
25
#define RED 1
26
#define BLACK 2
27
​
28
using namespace std;
29
​
30
pair<bool, int> Vertex[20001];
31
vector <int> Edge[20001];
32
//배열이 아닌 vector로 받는다.
33
​
34
bool coloring(int start, int color, int Vernum)
35
{
36
    queue <int> q;
37
​
38
    //처음에는 RED로 칠함.
39
    q.push(start);
40
    Vertex[start].first = true; Vertex[start].second = color;
41
​
42
    while (!q.empty())
43
    {
44
        int SelectVertex = q.front(); q.pop();
45
        for (int i = 0; i < Edge[SelectVertex].size(); i++)
46
        {
47
            int NeighborVertex = Edge[SelectVertex][i];
48
            if (!Vertex[NeighborVertex].first)
49
            {
50
                Vertex[NeighborVertex].first = true;
51
                if (Vertex[SelectVertex].second == BLACK)
52
                    Vertex[NeighborVertex].second = RED;
53
                else
54
                    Vertex[NeighborVertex].second = BLACK;
55
                q.push(NeighborVertex);
56
            }
57
            else
58
            {
59
                if (Vertex[SelectVertex].second == Vertex[NeighborVertex].second)
60
                    return false;
61
            }
62
        }
63
    }
64
    return true;
65
}
66
​
67
int main()
68
{
69
    int K; int V; int E;
70
    cin >> K;
71
    while (K--)
72
    {
73
        cin >> V >> E;
74
        for (int i = 0; i < 20001; i++)
75
            Edge[i].clear();
76
        for (int i = 0; i < 20001; i++)
77
            Vertex[i].first = Vertex[i].second = 0;
78
​
79
        int A; int B;
80
        for (int i = 0; i < E; i++)
81
        {
82
            scanf("%d %d", &A, &B);
83
            Edge[A].push_back(B);
84
            Edge[B].push_back(A);
85
        }
86
        int res = 0;
87
        for (int i = 1; i <= V; i++)
88
        {
89
            if(!Vertex[i].first)
90
                if (!coloring(i, RED, V))
91
                {
92
                    res = 1;
93
                    break;
94
                }
95
        }
96
​
97
        if (res)
98
            cout << "NO" << endl;
99
        else
100
            cout << "YES" << endl;
101
    }
102
}