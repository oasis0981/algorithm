def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper():
            answer += s.lower()
            continue
        answer += s.upper()
    return answer