def solution(my_string):
    arr = my_string.split(' ')
    result = int(arr[0])
    operator = ""
    for i in range(1, len(arr)):
        s = arr[i]
        if s.isdigit() == False:
            operator = s
            continue
        if operator == "+":
            result += int(s)
            continue
        if operator == "-":
            result -= int(s)
    return result