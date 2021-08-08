from collections import Counter


def solution(participant, completion):

    answer = list(Counter(participant)-Counter(completion))

    return answer[0]



participant=[["leo", "kiki", "eden"],["marina", "josipa", "nikola", "vinko", "filipa"],["mislav", "stanko", "mislav", "ana"]]

completion = [["eden", "kiki"],["josipa", "filipa", "marina", "nikola"],["stanko", "ana", "mislav"]]


for i in range(3):
    print(solution(participant[i],completion[i]))