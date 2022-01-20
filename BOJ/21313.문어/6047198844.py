N = int(input())
octopuses = [[True for _ in range(8)] for _ in range(N)]
res = []
for idx, cur_octopus in enumerate(octopuses):
    # 다음 문어가 존재하는지
    next_octopus = octopuses[(idx + 1) % N]

    for leg in range(8):
        if cur_octopus[leg] and next_octopus[leg]:
            cur_octopus[leg] = next_octopus[leg] = False
            res.append(leg+1)
            break
for leg in res:
    print(leg, end=' ')