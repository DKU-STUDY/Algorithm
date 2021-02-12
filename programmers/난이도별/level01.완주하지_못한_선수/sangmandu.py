def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, v in enumerate(completion):
        if v != participant[i]:
            return participant[i]
    return participant[-1]
