def card_conv(x:int, r:int) -> str:
    # 정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환

    d = ''  # 변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x%r]
        x //= r

    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            no = int(input("변환할 양의 정수를 입력하세요 : "))
            if no > 0:
                break

        while True:
            cd = int(input("어떤 진수로 변환할까요? : "))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry= input("한번더 변환할까요?(Y...예/N...아뇨): ")
        if retry in {'N', 'n'}:
            break