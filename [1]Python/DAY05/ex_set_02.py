# >>> set 자료형은 멤버 연산자가 가능함.

data_set = {1, 3, 5, 7, 9, 1, 3, 5, 7, 9}
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")

print(f"11 in data_set: {11 in data_set}\n")
print(f"11 not in data_set: {11 not in data_set}\n")

# >>> set 자료형 전용 메서드 
# >>> 원소/요소 1개 추가 메소드 add(data) -> 이미 존재하는 데이터면 추가하지 않음. 에러 발생 X

data_set.add(1) # 1이 이미 있기 때문에 실행 안함.
data_set.add(2)
data_set.add(3) # 3이 이미 있기 때문에 실행 안함.
data_set.add(4)

print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")

# >>> 원소/요소 여러 개 추가 메소드 update(반복이 가능한 데이터)
data_set.update([1, 2, 3, 4, 5, 10, 20, 30])
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")


data_set.update("GOOOOOD")  # str 중복 문자 제거됨.
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")

data_set.update(["GOOOOOD"])
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")


# >>> 원소/요소 삭제 메서드: remove(data)
data_set.remove("GOOOOOD")
print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")


data = data_set.pop()
print(f"{data}\n")

data = data_set.pop()
print(f"{data}\n")

data = data_set.pop()
print(f"{data}\n")

print(f"data_set: {len(data_set)}\n{type(data_set)}\n{data_set}\n")
