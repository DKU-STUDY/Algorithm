#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    const string dow[]={"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
    const int dom[]={31,29,31,30,31,30,31,31,30,31,30,31};
    int day=b;
    for(int i=0;i<a-1;i++){
        day+=dom[i];
    }
    return dow[day%7];
}
