
def recur_fun(i):
	if i == 10:
		return
	print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
	recur_fun(i+1)
	print(i, '번째 재귀함수 종료')

recur_fun(1)

# 스택에 함수를 넣었다가 빼는것처럼, 순서대로 호출하고 끝에것부터 종료됨
# 괄호를 쭉열고 닫는거 생각하면됨