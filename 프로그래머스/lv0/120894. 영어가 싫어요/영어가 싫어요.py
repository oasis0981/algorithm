def solution(numbers):
    n = {
        "one": 1,
        "two": 2,
        "three":3 ,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }
    strnum = numbers
    for number in n.keys():
        temp = strnum.replace(number, str(n[number]))
        strnum = temp
    return int(strnum)