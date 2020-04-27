def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
    if answer == '':
        answer = participant[-1]
    return answer
