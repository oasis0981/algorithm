def solution(my_string):
    result = 0
    for s in my_string:
        if s.isdigit() == False:
            my_string = my_string.replace(s, ' ')
    num_arr = my_string.split(' ')
    for n in num_arr:
        if n.isdigit():
            result += int(n)
    return result