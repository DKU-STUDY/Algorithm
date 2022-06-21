N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_width = min(N, M)

def get_square(max_width):
    for width in range(max_width, 0, -1):
        for y in range(N - width + 1):
            for x in range(M - width + 1):
                # 좌상 / 우상 / 좌하 / 우하
                left_top = arr[y][x]
                right_top = arr[y][x + width - 1]
                left_bottom = arr[y + width - 1][x]
                right_bottom = arr[y + width - 1][x + width - 1]
                if left_top == right_top == left_bottom == right_bottom:
                    return width * width
    return 1


print(get_square(max_width))

