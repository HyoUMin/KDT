## =======================================
## 컨테이너 자료형 - [1] List
## List와 연산자
## =======================================

# >>> 1 ~ 100 범위에서 7의 배수로만 구성된 데이터

num_list = range(7,31,7) # 타입이 range임 -> 형 변환 필요
num_list = list(num_list)
print(f"리스트: {num_list}    개수: {len(num_list)}개")
print()

# >>> 연산자 : List + List = NEW List
new_num_list = num_list + num_list
print(f"리스트: {new_num_list}   개수: {len(new_num_list)}개")
print()

# -------------------------------------
# >>> 연산자 : List - List 기능 지원 안함.
# >>> 연산자 : List * List 기능 지원 안함.
# -------------------------------------

# >>> 연산자 : List * int = 정수 숫자만큼 원소 반복. List 확장 기능. 새로운 List 반환
new_num_list = num_list * 3
print(f"리스트: {new_num_list}   개수: {len(new_num_list)}개")
print()

# >>> 시퀀스 연산자는 멤버 연산자 사용가능: 리스트, 튜플, 문자열
# >>> 연산자: 데이터 in list = 데이터가 list에 존재하는지 확인. 멤버연산자. True/False 반환 
print(f"8 in new_num_list => {8 in new_num_list}")
print(f"7 in new_num_list => {7 in new_num_list}")
print()

# >>> 연산자: 데이터 not in list = 데이터가 list에 존재 안하는지 확인. 멤버연산자. True/False 반환 
print(f"8 not in new_num_list => {8 not in new_num_list}")
print(f"7 not in new_num_list => {7 not in new_num_list}")
print()