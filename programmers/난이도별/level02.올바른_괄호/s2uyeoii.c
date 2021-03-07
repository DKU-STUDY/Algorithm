#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    int sum = 0;
    int len = strlen(s);
    
if(s[0]=='(' && s[len-1]==')'){
   for(int i = 0; i<len; i++)
    {
           sum = (s[i]=='(') ? (sum+1) : (sum-1);
           if(sum<0)
               return false;
           else
               continue;
    }
    if(sum==0) return true;
    else return false;
}
    else return false;
}
