def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n

    while start <= end:
        mid = (start + end) // 2

        tmp_n = 0
        for t in times:
            tmp_n += mid // t

        if tmp_n >= n:
            answer = mid
            end = mid - 1
        elif tmp_n < n:
            start = mid + 1

        # print(start, end, tmp_n)

    return answer