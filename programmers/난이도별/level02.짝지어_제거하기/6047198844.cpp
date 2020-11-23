#include <iostream>
#include <stack>
using namespace std;

int solution(string s)
{
    stack <char> st;
    for (char a_or_b : s) {
        if (st.empty()) {
            st.push(a_or_b);
            continue;
        }
        if (st.top() == a_or_b) {
            st.pop();
        }
        else {
            st.push(a_or_b);
        }
    }
    return !st.size();
}