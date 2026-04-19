# >>> 다양한 dict 데이터 생성 방식
# >>> zip() : 같은 위치에 있는 데이터를 하나로 묶어주는 기능
# 묶을 데이터 쌍이 없는 것은 실행안함.

names = ['홍', '박', '김']
score = [98, 100, 77]

result = zip(names,score)

print(f"result: {result}    type: {type(result)}\n")
# >>> 원하는 형식으로 출력하려면 형변환 필요함.
result = list(result)
print(f"result: {result}    type: {type(result)}\n ")

result = tuple(result)
print(f"result: {result}    type: {type(result)}\n ")

# >>> 딕셔너리는 2개까지만 가능함. 즉 키와 값 각각 1개씩만 가능함. 3개 이상은 불가능
result = dict(result)
print(f"result: {result}    type: {type(result)}\n ")