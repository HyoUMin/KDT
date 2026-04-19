# >>> 딕셔너리 추가 메소드

# >>> 딕셔너리 원소/요소 추기 메소드 -> 키:값 쌍으로 추가해야 함.
# >>> setdefault()
# >>> update() 

std_dict = {"홍길동": 3.9, "김길동": 4.1, "권길동": 2.7}
# >>> 원소 추가하가
std_dict.setdefault("박길동")
print(f"원소: {len(std_dict)}개, {std_dict}\n")


std_dict.setdefault("강길동", 3.3)
print(f"원소: {len(std_dict)}개, {std_dict}\n")

# >>> 이미 있는 키:값을 변경하지 않음.
std_dict.setdefault("강길동", 4.3) 
print(f"원소: {len(std_dict)}개, {std_dict}\n")

# >>> 존재하지 않는 키 추가해보기
# >>> 키는 str타입만 가능하고, str타입이지만 "", ''로 묶지 않음. 
std_dict.update(k = 2.9, p = 3.1, c = 4.0) 
print(f"원소: {len(std_dict)}개, {std_dict}\n")

# >>> 딕셔너리 형식으로 update() 사용하기
std_dict.update({'A': 1.3, 'Z': 3.9})
print(f"원소: {len(std_dict)}개, {std_dict}\n")

# >>> 키값 묶음으로 update() 사용하기
std_dict.update([['김', 3.2], ['이', 4.4]])
print(f"원소: {len(std_dict)}개, {std_dict}\n")

# >>> zip으로 묶은 후 update() 사용하기
std_dict.update(zip(['최', "제갈", "남궁"], [3.0, 2.9, 2.8]))
print(f"원소: {len(std_dict)}개, {std_dict}\n")


# >>> 원소요소 값 변경 -> update(키 값 묶음)사용. 키가 존재하면 업데이트 해주고, 여러 개도 가능함.

std_dict["홍길동"] = 2.7
std_dict["김길동"] = 3.0
print(f"원소: {len(std_dict)}개, {std_dict}\n")

std_dict.update(zip(["홍길동","김길동","권길동"], [2.2, 3.3, 1.1]))
print(f"원소: {len(std_dict)}개, {std_dict}\n")


# >>> 원소요소 삭제하기 -> pop(키) 키에 해당하는 값을 꺼내서 반환함. 
# >>>                   popitem() 마지막 원소를 꺼내서 (키, 값) 형태로 반환


val1 = std_dict.pop("홍길동")
print(f"원소: {len(std_dict)}개\n{std_dict}\n꺼낸 원소값: {val1}\n")


# >>> 마지막 원소 꺼내서 (키, 값) 형태로 가져오기
result = std_dict.popitem()
print(f"원소: {len(std_dict)}개\n{std_dict}\n꺼낸 원소값: {result}\n")

# >>> 특정 키의 원소 삭제: del 변수명[키]
del std_dict["제갈"]
print(f"원소: {len(std_dict)}개\n{std_dict}\n")

# >>> 모든 원소 지우기: clear()
std_dict.clear()
print(f"원소: {len(std_dict)}개\n{std_dict}\n")
