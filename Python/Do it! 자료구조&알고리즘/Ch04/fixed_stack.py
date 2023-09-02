# 고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack:

    class Empty(Exception):
        """비어있는 FixedStack에 팝 또는 피크할때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득찬 FixedStack에 푸시할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity        # 스택 본체
        self.capacity = capacity            # 스택의 크기
        self.ptr = 0                        # 스택 포인터

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():          # 스택이 가득 찬 경우
            raise FixedStack.Full   # 예외처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> Any:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비었습니다.')
        else:
            print(self.stk[:self.ptr])