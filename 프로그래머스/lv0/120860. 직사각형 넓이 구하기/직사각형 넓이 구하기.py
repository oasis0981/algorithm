def solution(dots):
    sorted_dots = sorted(dots, key = lambda x : [x[0], x[1]])
    min_dot, max_dot = sorted_dots[0], sorted_dots[-1]
    return (max_dot[0]-min_dot[0]) * (max_dot[1]-min_dot[1])