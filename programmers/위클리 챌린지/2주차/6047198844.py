def solution(scores):
    answer = ''

    def grade(avg):
        # print(avg)
        if avg >= 90:
            return 'A'
        elif 80 <= avg < 90:
            return 'B'
        elif 70 <= avg < 80:
            return 'C'
        elif 50 <= avg < 70:
            return 'D'
        else:
            return 'F'

    scores = list(zip(*scores))
    for idx, score in enumerate(scores):
        aggre = sum(score)
        N = len(score)
        self_score = score[idx]
        if score.count(self_score) == 1 and (self_score == min(score) or self_score == max(score)):
            aggre -= self_score
            N -= 1
        answer += grade(aggre // N)

    return answer