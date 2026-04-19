## =================================
## 표준 입출력 함수
## 입력함수: input()
## 출력함수: print()
## =================================

## ----------------------------------
# >>> print()
# >>> [1] 데이터 출력: print(data)
# >>> data + "\n"
print("[1]Good")
print()

# >>> print()
# >>> [2] 데이터 여러 개 출력: print(data1, data2, data3, ...)
# >>> data1 + data2 + data3 + ... + "\n"
print("[2]Good", 2026, "Happy")
print()

print("[3]Good", 2026, "Happy", sep = "경북대") # sep: 공백에 값 추가
print()

print("[4]Good", 2026, "Happy", end = " ") # 줄바꿈 X
print("[5]Good", 2026, "Happy")
print()

print("[6]Good", 2026, "Happy", end = "") # 줄바꿈 X
print("[7]Good", 2026, "Happy")
print()
# >>> data 원소가 10개
data = range(10) # 0 <= ~ < 10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("[8]", data, len(data),"개")
print("[9]", data, len(data), "개", sep="")
print()

# >>> [3] 입력 함수: input()
# >>> 반환값은 무조건 str 형태임.
new_str = input("첫 번째 숫자를 입력하세요: ")
print(f"입력값: {new_str}   타입 확인: {type(new_str)}")
print()

new_int = int(input("두 번째 숫자를 입력하세요: ")) # 형변환 필요
print(f"입력값: {new_int}   타입 확인: {type(new_int)}")
print()

new_float = float(input("세 번째 숫자를 입력하세요: ")) # 형변환 필요
print(f"입력값: {new_float}   타입 확인: {type(new_float)}")
