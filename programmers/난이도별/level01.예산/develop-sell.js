function solution(d, budget) {
  let answer = 0;
  let sort_arr = d.sort((a, b) => (a-b))
  let len = sort_arr.length
  let total_cost = 0;
  for(let i = 0; i < len; i++){
      if (total_cost + d[i] > budget)
          break;
      else{
          total_cost += d[i]
          answer++
      }
  }                   
  console.log(d)
  console.log(sort_arr)     
  return answer;
}

// 문제풀이: 
// 문제 조건 1) 최대한 많은 부서에게 물품을 구매할수록 있도록 한다 
// 문제 조건 2) 각 부서마다 비용이 다르다
// 문제 조건 3) 한 부서에게 지불해줄 시 신청한 금액 전체를 다 지원해줘야 한다.
//   (ex. 신청 금액이 5원인데, 4원만 지원 불가능)

// 가장 작은 비용의 부서부터 지원해줘야 최대한 많은 부서들에게 지원해주는 것이다. 
// 그래서 비용이 작은 순으로 부서별 비용 배열을 sort 시켰다. 
// 그 다음 for문을 돌면서 총 비용(total_cost)가 budget를 넘기 전까지 
// 부서들을 지원해주면 된다. 
// (부서 지원해주면 total_cost가 그 만큼 늘어나고(total_cost +=d[i]), 지원해준 부서 숫자(answer)도 늘어남)

// 궁금한 점: 
// 원래는 reduce 함수를 써서, 
// total 값이 budget을 넘지 않기 전까지의 answer 값을 구하려고 했는데, 
// 아직 개념이 헷갈려서 그런지 쉽지 않았다. 
// 그런데 생각해보니, reduce는 중간에 break 기능이 없어 배열은 엄청 긴데 비용이 높아 이제부턴 못 지원해주는 경우에 
// 모든 요소를 다 돌아야하니 덜 효율적이라고 생각했다. (for문은 break문으로 빠져나오기 때문)

// 그래도 reduce로 짜는 방법을 알고 싶은데, 
// 아래 코드까진 짜보았는데, 뭔가 문제가 있어 보입니다. 

// sort_arr.reduce((total, current) => ((total + current <= budget) ? (answer ++ , total+= current) : answer ), 0) 
// return answer 

// budget보다 작으면 돌면서 total 값에 current 값을 더하고, anwser++ 하는 건데, 
// 초기값은 0으로 지정해줬습니다. 무엇이 문제일까요? 

// 입력1: [1,2,3,4,5] , 9  / 정답1: 3  / 위 reduce 함수에서:  4
// 입력2: [2,2,3,4] , 10   / 정답2: 4  / 위 reduce 함수에서:  4 


// 알게 된 점: 
// 위에 식에서 14,15줄을 보면 내가 sort한 arr를 sort_arr로 두게 되었는데,
// 실수로 for문 안에서는 d 배열로 돌리게 되어 틀릴 줄 알았는데, 맞았다. 
// 즉, sort() 함수는 하는 순간 바로 그 배열 자체에서 sort가 적용된다. 
// ex. let arr1 = arr2.sort()   ===> 이때 arr1, arr2의 값이 동일해진다. 




 