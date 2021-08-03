def solution(n, build_frame):
    structures = set()

    def is_valid():
        for structure in structures:
            x, y, kind = structure
            if kind == 1:
                if not ((x, y - 1, 0) in structures or (x + 1, y - 1, 0) in structures or (
                        (x - 1, y, 1) in structures and (x + 1, y, 1) in structures)):
                    return False
            else:
                if not (y == 0 or (x, y - 1, 0) in structures or (x - 1, y, 1) in structures or (
                x, y, 1) in structures):
                    return False
        return True

    for frame in build_frame:
        x, y, kind, cmd = frame
        # 삽입
        if cmd == 1:
            structures.add((x, y, kind))
            if not is_valid():
                structures.remove((x, y, kind))
        # 삭제
        else:
            structures.remove((x, y, kind))
            if not is_valid():
                structures.add((x, y, kind))

    answer = list(structures)
    answer.sort()
    return answer