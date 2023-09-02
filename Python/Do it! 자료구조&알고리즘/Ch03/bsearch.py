#  이진탐색 : 데이터가 오름차순이나 내림차순으로 정렬되어 주어질 때 사용함

from typing import Any, Sequence

def bin_search(a : Sequence, b : Any) -> int:

    pl = 0
    pr = len(a)-1

    while True:
        pc = (pr+pl)//2
        if a[pc] == b: return pc

        if a[pc] < b: pl = pc+1
        else : pr = pc-1

        if pl > pr: break
    return -1

if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    print('배열 데이터 오름차순 입력')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i-1]:
                break   # 직전에 입력한 원소보다 큰 값을 입력받지 않으면 다시 입력 받음

    ky = int(input('검색 값을 입력 : '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('존재X')
    else:
        print(f'해당 원소는{idx}에 있음')
