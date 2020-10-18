function solution(n, m) {
    let r,a,b;
    a=Math.max(n,m);
    b=Math.min(n,m);
    do{
        r=a%b;     //큰값에서 작은값을 나눈 나머지를 r에 저장
        a=b;        //a를 b로 변환
        b=r;        //b를 r로 변환
    }
    while(r!=0)

    return [a].concat([m*n/a])    // a%b가 0이되었을때의 나누는수 b는 a=b로 인해 a이므로 최대공약수는 a 최소공배수는 m*n/a이다.
}
// 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12940

//최소공배수 최대공배수 관련내용
//2개의 자연수  a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면 (단 a>b),
// a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 이 성질에 따라, b를 r로 나눈 나머지 r0를 구하고,
// 다시 r을 r0로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
// 이는 명시적으로 기술된 가장 오래된 알고리즘으로서도 알려져 있으며, 기원전 300년경에 쓰인 유클리드의 <원론> 제7권, 명제 1부터 3까지에 해당한다.

//출처 : https://myjamong.tistory.com/138


