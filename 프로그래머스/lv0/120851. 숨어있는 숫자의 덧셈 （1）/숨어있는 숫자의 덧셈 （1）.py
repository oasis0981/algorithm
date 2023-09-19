def solution(my_string):
    sum = 0 
    for s in my_string:
        if s.isdigit():
            sum += int(s)

    return sum