//성공은 했으나 코드 좀 부족

function solution(citations) {
    var answer = 0;
    let a=[];
    let b=[];
    citations.sort((A,B)=>A-B);

    for(let i=citations.length;i>0;i--)
    {
        for(let j=0;j<citations.length;j++)
        {
            if(citations[j]>=i){
                a = citations.slice(0,j);
                b = citations.slice(j,citations.length);

                if(a.length<=i&&b.length>=i){
                    return i;
                }
            }
        }
    }
    return 0;

}

//다른사람 코드

function solution(citations) {
    citations = citations.sort(sorting);
    var i = 0;
    while(i + 1 <= citations[i]){
        i++;
    }
    return i;


    function sorting(a, b){
        return b - a;
    }
}

/*
개인적으로 문제가 조금 이상하다고 느낀다.
예를 들어 [10,9,8,7,6,5,4,3,2,1,1,1,1]이 주어진다면 실행한 결과값이 5가 나오지만
'어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.'
라고 주어진 문제에서
이 부분에서 5번 이하로 인용이 되지않으므로 위에서 제시한 코드들이 문제가 될거라 생각이된다.
아마 1,1,1,1 이러한 것이 없이 서로 다른 인용횟수 라고 정해진다면 문제가 없을거라 생각한다.
 */

//출처 : https://programmers.co.kr/learn/courses/30/lessons/42747#
