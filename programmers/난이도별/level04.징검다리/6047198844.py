def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    # 정답의 범위
    begin = 0
    end = distance

    #    print(rocks)
    while begin <= end:
        # 우리가 목표하는 거리
        mid = (begin + end) // 2
        # 현재 남아있는 바위의 위치
        stack = [0]

        for rock in rocks:
            # 현재 거리와 stack위의 rock거리를 비교
            between = rock - stack[-1]
            if between < mid:
                # 제거해야한다.-> stack에 넣지 않는다.
                continue
            stack.append(rock)

        # 마지막돌과 도착지점의 거리를 계산한다.
        # 해당 거리가 우리가 목표하는바 보다 작다면 해당 돌을 제거한다.
        last_distance = distance - stack[-1]
        if last_distance < mid:
            stack.pop()
        stack.append(distance)

        min_distance = distance

        # 돌간 최소거리
        for idx in range(1, len(stack)):
            min_distance = min(min_distance, stack[idx] - stack[idx - 1])

        # 삭제한 돌의 개수 (출발지점은 제외함)
        del_rock_n = len(rocks) - (len(stack) - 2)
        if del_rock_n <= n:
            # 삭제한 돌이 N보다 작은경우 -> 거리가 짧으므로 거리를 늘린다.
            # 삭제한 돌이 N인경우 -> 정답 갱신
            answer = max(answer, min_distance)
            begin = mid + 1
        # 삭제한 돌이 N보다 큰경우 -> 거리가 기므로 거리를 좁힌다.
        else:
            end = mid - 1
    return answer