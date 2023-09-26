def solution(sides):
    i=1
    triangle = sorted(sides + [i])
    answer = 0
    while (True):
        if triangle[2] == i and triangle[2] >= triangle[0] + triangle[1]:
            break
        if triangle[2] < triangle[0] + triangle[1]:
            answer += 1
        i += 1
        triangle = sorted(sides + [i])
    return answer