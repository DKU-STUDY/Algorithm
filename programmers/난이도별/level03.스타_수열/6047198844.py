from collections import Counter


def solution(a):
    answer = 0
    # 부분수열은 원래 순서을 유지하여 얻을 수 있는 a를 포함한 a의 부분집합이다.
    stars = Counter(a).most_common()
    for star, N in stars:
        # 스타를 기준으로 구함.
        # 현재 스타로 만들수있는 최대 스타 수열이 answer보다 같거나 작을 경우 가지치기
        if N * 2 <= answer:
            return answer

        star_count = 0
        idx = 0
        while idx < len(a) - 1:
            if a[idx] != a[idx + 1] and (star == a[idx] or star == a[idx + 1]):
                # 수열에 추가
                star_count += 2
                # 현재 구간은 수열에 소모됬으므로 idx를 두번 더한다.
                idx += 1
            idx += 1

        answer = max(star_count, answer)

    return answer