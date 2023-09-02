def solution(l):
    len = 0
    len += l[0][1] - l[1][0] if l[0][1] - l[1][0] > 0 else 0
    len += l[1][1] - l[2][0] if l[1][1] - l[2][0] > 0 else 0
    len += l[2][1] - l[0][0] if l[2][1] - l[0][0] > 0 else 0
    min_end = min([line[1] for line in l])
    max_start = max([line[0] for lien in l])
    if min_end > max_start:
        len -= min_end - max_start
    return len