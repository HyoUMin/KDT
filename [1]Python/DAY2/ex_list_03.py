## =================================================
## 컨테이너 자료형 - [순서 있는 자료형] list
## -> 다양한 내장 함수 사용하기
## ==================================================

# 리스트 생성하기
# ---------------------------------------------------

# >>> 기본 리스트 형태
scores_list1 = [90, 89, 100, 79, 99]
scores_list2 = list([90, 89, 100, 79, 99])

print(scores_list1)
print(scores_list2)
print()
print()

# >>> 다양한 데이터를 리스트에 저장하기
data1 = []
data2 = [23, 123, -3, 0.98, 99.999]
data3 = ["Abc", "APPle", "anaconda", "zoo"] 


# >>> 내장함수: sorted(변수명) -> 데이터/요소들 정렬 후 반환 함수
# > 항상 list로 반환하고, 오름차순이 기본값
print("오름차순: 작은 값 -> 큰 값")
print(f"sorted(data1):    {sorted(data1)}          {data1}")
print(f"sorted(data2):    {sorted(data2)}          {data2}")
print(f"sorted(data3):    {sorted(data3)}          {data3}")
print()
print()

# >>> 내림차순으로 정렬하기
print("내림차순: 큰 값 -> 작은 값")
print(f"sorted(data1):    {sorted(data1,  reverse = True)}          {data1}")
print(f"sorted(data2):    {sorted(data2,  reverse = True)}          {data2}")
print(f"sorted(data3):    {sorted(data3,  reverse = True)}          {data3}")
print()
print()


# >>> 내장함수: range(시작값, 마지막값 + 1, 간격) -> 데이터 범위 생성 후 반환 함수
# > 많은 데이터 생성 시 사용하는 함수
# > 데이터 범위 객체/타입 생성
# > 데이터 범위: 시작값 <= ~ < 마지막값
# > EX) 1부터 1000까지 OR 1 ~ 1000 => [1, 2, 3, 4, ..., 1000]
# >                               => range(1, 1001)

# >>> 1부터 10까지 숫자 데이터 저장
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = range(1, 11)
print(f"data1: {data1}      {len(data1)}개        {type(data1)}")
print(f"data2: {data2}      {len(data2)}개        {type(data2)}")
print()
print()

# >>> 1부터 30까지 숫자 중 3의 배수만 데이터 저장
data1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
data2 = range(3, 31, 3)
print(f"data1: {data1}      {len(data1)}개        {type(data1)}")
print(f"data2: {data2}      {len(data2)}개        {type(data2)}     {list(data2)}")
print()
print()

# >>> 50부터 1까지 범위의 숫자를 출력하세요. 단, range 함수 사용
data_range = range(50, 0, -1)
print(f"data_range: {data_range}")
print(f"data_range: {list(data_range)}")
print()
print()

# >>> 리스트로 형 변환 후 내림차순 정렬하기
data_range_reverse = range(1, 51)
print(f"data_range_reverse: {data_range}")
print(f"data_range_reverse: {sorted(list(data_range), reverse = True)}")
print()
print()