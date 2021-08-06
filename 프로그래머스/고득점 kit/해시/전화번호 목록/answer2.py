
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1,p2 in zip(phoneBook,phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book=[["119", "97674223", "1195524421"],["123","456","789"],["12","123","1235","567","88"]]


for i in range(len(phone_book)):
    print(solution(phone_book[i]))