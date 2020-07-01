function solution(S) {
    const A=S.length;
    S=[...S];                           //문자열을 배열로 선언
    for(let i=0;i<A;i++)
    {
        if(S[i]=='('&&S[i+1]==')')      // 어떠한 값과 다음값이 ()를 형성하면
        {
            S.splice(i,2);          //S배열에서 제거
            if(S.length==0)         //S배열이 공백이면 for문 종료
                break;
            i-=2;                   //i++을 나중에 하므로 그 전꺼까지 계산위해서 i를 2감소
        }
    }
    return (S.length==0)? 1 : 0;        //공백이면 1리턴 뭔가 남아있으면 0 리턴
}

console.log(
    solution('(()(())())') === 1,
    solution('())') === 0,
    solution('((())') === 0,
    solution('((()))))') === 0,
);