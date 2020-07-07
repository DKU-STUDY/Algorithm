//방법1 : 정확성은 맞으나 효율성 부족
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

//방법2 : 정확성 효율성 전부 문제x
function solution(S) {
    let k=[];
    const s_size=S.length;
    for(let i=0;i<s_size;i++)
    {
        if(S[i]=='(')
            k.push('(');            //S[i]가 '('이면 k에 '('넣기
        else{
            if(k.length==0)         //S[i]가 ')'이면 k에 남은 것이 없으면 연결이 안되므로 0리턴 ())
                return 0;
            k.pop();                //남은것이 있으면 그 값 처리
        }
    }
    return (k.length==0)?1:0;       //전부연결되어 서로 상쇄돼 다 없어지면 1리턴 남은게 존재하면 0리턴
}


console.log(
    solution('(()(())())') === 1,
    solution('())') === 0,
    solution('((())') === 0,
    solution('((()))))') === 0,
);