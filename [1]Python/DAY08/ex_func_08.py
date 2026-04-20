# ===== ===== ===== ===== =====
# >>> 사용자 정의 함수: 함수 이름과 class function
# >>> 함수 이름: 실행코드의 주소를 가지고 있음. 다른 변수에 저장될 수 있음.
# >>> 내장 함수를 변수로 사용시 기존 내장함수 기능을 사용하지 못함.
# ===== ===== ===== ===== =====

# >>> EX. 10개의 숫자 데이터 중에서 최댓값, 최솟값, 합계를 출력
datas = [4, 2, 6, 7, 32, 13, 43, 22, 5, 8, 1]
func_list = [max, min, sum, sorted]

print(max(datas), min(datas), sum(datas))
print(func_list[0](datas), func_list[1](datas), func_list[2](datas), func_list[3](datas))

# >>> 함수 이름을 다른 변수에 저장하기
total = sum
print(total(datas), sum(datas))

# >>> 함수 이름에 새로운 데이터를 저장하면 그 함수는 사용불가함.
# sum = 202  사용 불가함.
# print(sum(datas))

# >>> 같은 변수명의 지역변수와 전역변수

num = 100

def change(a, b, num):
    num = num * (a + b) 
    print(a, b, num)

print(num)
change(1, 2, 3)
print(num)