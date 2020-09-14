#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long num) { //마지막 테스트 케이스가 int범위 초과 
    
    for(int answer=0; answer<500; answer++)
    {
        if(num==1)
            return answer;
        else
            num = (num%2==0) ? (num/2) : (num*3+1);
        
    }
    return -1;
}
