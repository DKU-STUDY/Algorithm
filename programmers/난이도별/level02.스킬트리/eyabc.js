/**
 * 스킬트리
 * 문제 : https://programmers.co.kr/learn/courses/30/lessons/49993
 * @param skill 선행 스킬 순서  / 알파벳 대문자 (1~26자) 중복스킬 없음,
 * @param skill_trees 유저들이 만든 스킬트리 (1~20개) (2~26자)
 * return : 가능한 스킬트리 개수
 *
 * 아이디어
 */


function solution(skill, skill_trees) {
  const reg = new RegExp(`[${skill}]`, 'g');

  return skill_trees.reduce((cnt, user_skill) => {
    const found = user_skill.match(reg);

    const res = found
      && found.every((user, j) => user === skill[j]);

    if (res || !found) cnt++;

    return cnt
  }, 0);
}

console.log(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']) === 2);
console.log(solution('C', ['A']) === 1);

// 8개월 전에 푼것?
function solution2(skill, skill_trees) {
  let cnt = 0;
  let str = skill.split('');
  let tree = skill_trees.map((i, ki) => {
    let re = new RegExp(`[${str}]`);
    if (!re.exec(i)) cnt++;
    return i.split('');
  }).forEach(i => {
    let que = [];
    i.forEach((j, jk) => str.forEach(k => k === j ? que.push(j) : ''));
    que.some((q, qk) => {
      if (q !== str[qk]) {
        return true;
      }
      else if (q === str[qk] && qk === que.length - 1) {
        cnt++;
      }
    });
  });
  return cnt;
}