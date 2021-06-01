function solution(n, works) {
  works.sort((a,b)=>(b-a))

  if(works.reduce((acc,val)=>acc+val ,0) < n )
    return 0;

  while(n>0)
  {
    for(let i=0;;i++)
    {
      works[i]--;
      n--;
      if(works[i]+1 !== works[i+1] || n===0)
        break;
    }
  }
  return works.reduce((acc,val)=>acc+val*val ,0);
}

//문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12927#
//코드 정리 : https://velog.io/@khw970421/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%BC%EA%B7%BC-%EC%A7%80%EC%88%98
