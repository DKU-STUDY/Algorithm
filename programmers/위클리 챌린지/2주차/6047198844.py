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
        self_score = scores[idx][idx]
        print(score.count(self_score))
        if scores[idx].count(self_score) == 1 and (self_score == min(scores) or self_score == max(scores)):
            print(scores[idx][idx])

    return answerv