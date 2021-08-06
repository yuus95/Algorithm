# 다른사람 풀이
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False

    return True



phone_book=[["119", "97674223", "1195524421"],["123","456","789"],["12","123","1235","567","88"]]


for i in range(len(phone_book)):
    print(solution(phone_book[i]))