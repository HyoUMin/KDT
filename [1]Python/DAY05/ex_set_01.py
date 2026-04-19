# >>> 컨테이너 자료형 - Set
# >>> 중복 데이터는 저장되지 않음.
# >>> 원소/요소 식별용 인덱스 없음.
# >>> 형식: {원소1, 원소2, ..., 원소n}
# >>> 빈 집합: set() // {} -> 딕셔너리임. set과 혼동하면 안됨.

data_set = {1, 1, 1, 1, 1, 1, 1, 1}
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")

data_set = {1, 2, 3, 4, 5, 6, 7}
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")

# >>> 빈 Set 객체 생성하기
data_set1 = {}
data_set2 = set()
print(f"data_set1: {len(data_set1)}\n{type(data_set1)}\n{data_set1}\n")

print(f"data_set2: {len(data_set2)}\n{type(data_set2)}\n{data_set2}\n")
