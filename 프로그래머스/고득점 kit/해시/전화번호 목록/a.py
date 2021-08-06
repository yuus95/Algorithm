# 83점 다시풀기 
def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        # 전화번호 길이
        le = len(phone_book[i])

        for j in range(i+1,n):
            next_le = len(phone_book[j])
            text = phone_book[j]
            for k in range(len(text)):
                if k+le < next_le:
                    if phone_book[i] == text[k:k+le]:
                        return False
                else:
                    if phone_book[i] == text[k:]:
                        return False

    return answer





phone_book=[["119", "97674223", "1195524421"],["123","456","789"],["12","123","1235","567","88"]]


for i in range(len(phone_book)):
    print(solution(phone_book[i]))