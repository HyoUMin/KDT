# >>> 파이썬 표준 패키지
# ===== ===== ===== ===== =====
# os 모듈
# ===== ===== ===== ===== =====

import os

# os.mkdir()
# 1개 폴더 생성
# 존재하면 에러 발생
# os.mkdir("test")

# os.makedirs()
# 여러 단계 즉, 모든 경로 파일 생성
# exist_ok = True
# 이미 존재하면 생성하지 않음 -> 에러 발생하지 않음
os.makedirs("a/b/c", exist_ok = True)

# os.lisdir()
# 폴더 내의 목록이름 리스트 반환
items = os.listdir("../DAY10")
print(len(items), '\n')
print(items)
print()

# os.join()
# 경로만들기
i_path = os.path.join("../DAY10", items[0])
print(i_path)

i_path = os.path.join("../DAY10", items[0],"image.jpg")
print(i_path, '\n')


# DAY10 폴더 안의 파일만 화면에 출력하세요.
# 단, 경로정보까지 출력해주세요.(예시: ../DAY10/test.py)
items = os.listdir("../DAY10")
for item in items:
    item_path = os.path.join("../DAY10", item)
    if os.path.isfile(item_path):
        print(item, os.path.join("../DAY10", item))


import random as rd
# random.random() 0 이상 1 미만 실수 무작위 반환
print(rd.random(), rd.random(), rd.random()) 

# random.randint(a, b) a 이상 b 이하 정수 무작위 반환
print(rd.randint(1, 10), rd.randint(1, 10)) 

# random.randrange(start, stop, step) 정수
print(rd.randrange(1, 10),rd.randrange(1, 10, 2)) 

# random.uniform(start, stop) 실수
print(rd.uniform(1, 10), rd.uniform(1, 10))


# random.choice(순서 있는 데이터 타입) 1개 무작위 반환
print(rd.choice([1, 2, 3]), rd.choice([1, 2, 3]))

# random.choices(순서 있는 데이터 타입, k = n) n개 무작위 반환. 중복 허용
print(rd.choices([1, 2, 3], k = 5))

# random.sample(순서 있는 데이터 타입, k = n) n개 무작위 반환. 중복 불허
print(rd.sample([1, 2, 3], k = 2))

# random.seed() 매번 동일한 랜덤값 추출하도록 고정
rd.seed(10)
print("seed 고정")
print(rd.sample(range(1, 46), k = 6))