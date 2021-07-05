import collections


def solution(genres, plays):
    answer = []

    table = collections.defaultdict(list)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        table[genre].append((int(play), int(idx)))

    stable = sorted(table.items(), key=lambda x: sum([y[0] for y in x[1]]), reverse=True)

    for type in stable:
        for v in sorted(type[1], key=lambda x: (x[0], -x[1]), reverse=True)[:2]:
            answer.append(v[1])
    # 같으면 낮은 순으로! 즉 reverse되면 높은순이된다.
    return answer