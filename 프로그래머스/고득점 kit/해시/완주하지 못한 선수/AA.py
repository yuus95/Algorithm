from collections import Counter


# 카운터 클래스 끼리 마이너스 연산을 지원한다.
# 딕셔너리를 리스트로 만들면 키값이 반환된다.
# 값이 필요할떈 list(dict.values())
# 딕셔너리 자체가 값을 뺼 수 잇다.
def solution(participant, completion):
    answer = list(Counter(participant)-Counter(completion))

    return  answer[0]




participant=[["leo", "kiki", "eden"],["marina", "josipa", "nikola", "vinko", "filipa"],["mislav", "stanko", "mislav", "ana"]]

completion = [["eden", "kiki"],["josipa", "filipa", "marina", "nikola"],["stanko", "ana", "mislav"]]


for i in range(3):
    print(solution(participant[i],completion[i]))