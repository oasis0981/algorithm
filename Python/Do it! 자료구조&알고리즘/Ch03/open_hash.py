# 오픈 주소법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0    # 데이터가 저장된 상태
    EMPTY = 1       # 비어있는 상태
    DELETED = 2     # 삭제된 상태


class Bucket:
    """ 해시를 구성하는 버킷 """

    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        """ 초기화 """
        self.key = key              # 키
        self.value = value          # 값
        self.stat = stat            # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """ 모든 필드에 값을 설정 """
        self.key = key              # 키
        self.value = value          # 값
        self.stat = stat            # 속성

    def set_status(self, stat:Status) -> None:
        """ 속성을 설정 """
        self.stat = stat


class OpenHash:
    """ 오픈 주소법으로 구현하는 해시 클래스 """

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        """ 해시 값을 구함 """
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key:Any) -> int:
        """ 재해시값을 구함 """
        return(self.hash_value(key) + 1) % self.capacity

    def search_node(self, key:Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:    # 데이터 저장 상태이고 키가 key와 같은경우 그 버킷을 return
                return p
            hash = self.rehash_value(hash)                      # 재해시
            p = self.table[hash]
        return None

    def search(self, key:Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:       # 저장상태이고 키가 key인경우
            return p.value      # 검색 성공
        else:                   # EMPTY or DELETED
            return None         # 검색 실패

    def add(self, key:Any, value:Any) -> bool:
        """ 키가 key이고 값이 value인 원소를 추가 """
        if self.search(key) is not None:           # 저장상태이고 키가 key인경우
            return False                           # 추가 실패

        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False               # 저장할 공간 못찾은 경우 return False

    def remove(self, key:Any) -> int:
        """ 키가 key인 원소를 삭제 """
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2}', end = '')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value}')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i].stat == Status.DELETED:
                print('-- 삭제 완료 --')

