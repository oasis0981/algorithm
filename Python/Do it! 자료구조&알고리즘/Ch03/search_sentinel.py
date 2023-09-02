from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key:Any) -> int:
    #보초법으로 key와 일치하는 원소를 선형 검색
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(a) else i

if __name__ == "__main__" :
    num = int(input("원소 수 입력 : "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}] = "))

    ky = int(input("찾을 값 입력 : "))

    idx = seq_search(x,ky)

    if idx == -1:
        print("찾는 값이 목록에 없음")
    else:
        print(f"찾는 값은 {idx}번째 인덱스에 있음")
