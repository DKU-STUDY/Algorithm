#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    
    for(int i = 0, len = phone_number.length();  i < len - 4; i++)
    {
        phone_number[i] = '*';
}
    return phone_number;
}
