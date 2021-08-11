def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()

    begin = min(rocks)
    end = distance

    while begin < end:
        print(begin, end)
        min_distance = distance
        mid = (begin + end) // 2
        stack = [0]

        for rock in rocks:
            # 현재 거리와 stack위의 rock거리를 비교
            if rock - stack[-1] < mid:
                # 제거해야한다.-> stack에 넣지 않는다.
                pass
            else:
                stack.append(rock)
                if stack[-1] - stack[-2] < min_distance:
                    min_distance = stack[-1] - stack[-2]

        # 삭제한 돌의 개수
        del_rock_n = len(rocks) - len(stack)
        if del_rock_n <= n:
            # 삭제한 돌이 N보다 작은경우 -> 거리가 짧으므로 거리를 늘린다.
            # 삭제한 돌이 N인경우 -> 정답 갱신
            if del_rock_n == n:
                answer = min_distance
            begin = mid + 1
        # 삭제한 돌이 N보다 큰경우 -> 거리가 기므로 거리를 좁힌다.
        elif del_rock_n > n:
            end = mid - 1

        print(stack, answer)

    return answer