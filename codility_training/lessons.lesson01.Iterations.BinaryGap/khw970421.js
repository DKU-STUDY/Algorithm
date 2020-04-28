
방법 1 (방법 2에 비해 if문대신 Math.amx,삼항연산자로 코드를 간결화 for문 대신 while문으로 대체 result라는 불필요 변수 제거) 

function solution(N) {
  const a = N.toString(2);                                  //배열생성 N이 32일경우 a는 100000
  let i = 0, len = a.length, max_result = 0;                
  while (i < len) {
    idx = a.indexOf('1', i + 1);                        // 문자열을 탐색 a.indexOf('1',i)부터 안해도 첫번째는 1이고 그외에는 N이 0인값이다.
    if (idx === -1) break;
    max_result = Math.max(idx - i, max_result);     //첫번째 이후 처음 찾은 1에서 첫번째의 1을 뺀값을 비교하며 그후는 반복하며 가장큰 값찾는다.
    i = idx;                                        //불필요한 i의 반복을 막기위해 찾은 idx를 i로 하여 반복문을 다시 돌린다.
  }
  return max_result === 0 ? 0 : max_result - 1;     //max_result가 0일경우는 a가 1111일경우 혹은 0일경우다. 그외에는 값이 존재 
                                                    // 1과1 사이에 있는 갯수이기에  max_result - 1 로 처리
}

방법 2
function solution(N) {
    let a,b=[];//배열생성
    let p=0;
    let max_result=0,result=0;
    
     a=N.toString(2);
     const a_length=a.length;
     for(let i=0;i<a_length;)
     {
         idx = a.indexOf(1,i+1);
         if(idx== -1) break;
         
         gap_result = idx-result;
         if(max_result<gap_result) max_result=gap_result;
         result=idx;
         i=idx;
     }
     if(max_result>=1)
     return max_result-1;
     else
     return 0;
    //성공
}
