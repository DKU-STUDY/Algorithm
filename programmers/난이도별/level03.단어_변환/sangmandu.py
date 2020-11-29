'''
https://programmers.co.kr/learn/courses/30/lessons/43163
단어 변환 : 한글자만 변경하면 같아지는 글자를 찾아 이동하면서 원하는 단어를 구할 때의 이동횟수를 구하는 문제
1) 모든 단어는 50개 이하이므로 51개와 min 비교 가능
2) 선택된 단어는 words에 제거되며 words의 크기인 length로 이동횟수 파악 가능
이 때, words는 mutable 하므로 slicing한 words를 인자로 결정
3) 매번 len을 조사하는 시간을 조금이나마 줄이고자 lenWord와 lenWords 그리고 length 사용
'''


def solution(begin, target, words):
    if target not in words: return 0
    lenWord = len(begin)
    lenWords = len(words)

    def cal(begin, words, length):
        if begin == target:
            return lenWords - length
        if not length: return 51
        answer = [51]
        for idx, word in enumerate(words):
            if [word[i] == begin[i] for i in range(lenWord)].count(True) == lenWord - 1:
                answer.append(cal(word, words[:idx] + words[idx + 1:], length - 1))
        return min(answer)

    answer = cal(begin, words, len(words))
    return answer if answer != 51 else 0


'''
처음에는 set.intersection을 이용해서 한자리가 틀린지 확인했다.
hhx =? hih 같은 단어가 True로 처리되는 걸 질문게시판에서 알았고 결국 개별 인덱스를 비교했음.
'''