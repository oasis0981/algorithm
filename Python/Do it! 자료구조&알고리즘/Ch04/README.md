# Stack and Que

## 1. Stack

데이터 임시 저장할 때 사용

- 후입 선출
- 푸시로 넣고, 팝으로 꺼냄

### 고정길이 스택 구현하기

`stk` : 스택 본체 list형 배열

`capacity` : 스택 최대 크기

`ptr` : 스택 포인터 - 스택에 쌓여있는 데이터의 개수

`Empty`, `Full` : 예외처리 클래스

`push()` : 데이터 추가 - 가득찼을 경우 FixedStack.Full으로 예외처리

`pop()` : 스택의 꼭대기에서 데이터를 꺼내 return - 비었을 경우 예외처리

`peek()` : 스택의 꼭대기 데이터 들여다보기 - 비었을 경우 예외처리

`find()` : stk안에 value와 같은 값이 있는지 검색 - 꼭대기 → 바닥으로 선형 검색

`count()` : stk 내의 value 데이터 개수 세기 

`__len__()` : 쌓여 있는 데이터 개수 확인 - 연산자 `len()`사용 가능

`__contains__()` : stk내에 value가 있는지 판단 - 연산자 `in` 사용 가능

`dump()` : 모든 데이터 출력

```text
💡 raise문을 통한 예외처리
- 표준 내장 예외 처리 : BaseException 클래스 (ValueError, ZeroDivisionError 등)
- 사용자 정의 예외 처리 : Exception클래스(또는 그 파생 클래스)에서 파생하는 것이 원칙
```
```text
💡 더블 언더스코어를 줄여서 던더라고도 한다.
```



