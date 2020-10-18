function solution(num) {
    let a=0;
    if(num==1)
        return 0;
    do {
        num=(num%2==0)?(num/2):(num*3+1);
        a++;
    }
    while(num!=1)
    return (500>a)?a:-1;
}

// 출처 : https://programmers.co.kr/learn/courses/30/lessons/12943
