# ================================================================
#  Python 조건부 표현식 실습 문제집
#  Conditional Expression (Ternary Operator)

#  형식: [참일 때 값] if [조건] else [거짓일 때 값]
# ================================================================


# ----------------------------------------------------------------
#  ★ 초급 (Beginner) - 기본 조건부 표현식
# ----------------------------------------------------------------

# [문제 1]
# 정수 n을 입력받아, n이 양수이면 "양수", 그렇지 않으면 "양수 아님"을 출력하세요.
# 조건부 표현식 한 줄로 작성하세요.

#   n = 7
#   result = ???
#   예상 출력: "양수"

#   n = -3
#   result = ???
#   예상 출력: "양수 아님"

n = 7
print("[문제 1]: n = 7 -> ", "양수" if n > 0 else "양수 아님","\n")

n = -3
print("[문제 1]: n = -3 ->", "양수" if n > 0 else "양수 아님","\n")


# [문제 2]
# 정수 n이 짝수이면 "even", 홀수이면 "odd"를 반환하는
# 조건부 표현식을 작성하세요.

#   n = 4  → "even"
#   n = 7  → "odd"

n = 4
print("[문제 2]: n = 4 -> ", "even" if not n % 2 else "odd","\n")

n = 7
print("[문제 2]: n = 7 -> ", "even" if not n % 2 else "odd","\n")


# [문제 3]
# 두 수 a, b 중 더 큰 수를 반환하는 조건부 표현식을 작성하세요.
# (내장 함수 max() 사용 금지)

#   a, b = 10, 20  → 20
#   a, b = 35, 12  → 35

a, b = 10, 20
print("[문제 3]: a, b = 10, 20 -> ", a if a > b else b,"\n")

a, b = 35, 12
print("[문제 3]: a, b = 35, 12 -> ", a if a > b else b,"\n")


# [문제 4]
# 변수 is_raining이 True이면 "우산을 챙기세요", False이면 "우산 불필요"를
# 출력하는 조건부 표현식을 작성하세요.

#   is_raining = True   → "우산을 챙기세요"
#   is_raining = False  → "우산 불필요"

is_raining = True
print("[문제 4]: is_raining = True -> ", "우산을 챙기세요" if is_raining else "우산 불필요","\n")

is_raining = False
print("[문제 4]: is_raining = False -> ", "우산을 챙기세요" if is_raining else "우산 불필요","\n")


# [문제 5]
# 문자열 name이 빈 문자열("")이면 "이름 없음", 아니면 name 값을 그대로
# 반환하는 조건부 표현식을 작성하세요.

#   name = "홍길동"  → "홍길동"
#   name = ""          → "이름 없음"

name = "홍길동"
print("[문제 5]: name = 홍길동 -> ", name if len(name) else "이름 없음","\n")

name = "" 
print("[문제 5]: name = ""  -> ", name if len(name) else "이름 없음","\n")


# [문제 6]
# 정수 n이 0이면 "영", 0이 아니면 "0 아님"을 반환하는
# 조건부 표현식을 작성하세요.

#   n = 0   → "영"
#   n = 5   → "0 아님"
#   n = -1  → "0 아님"

n = 0
print("[문제 6]: n = 0 -> ", "영" if n == 0 else "0 아님","\n")

n = 5 
print("[문제 6]: n = 5 -> ", "영" if n == 0 else "0 아님","\n")


n = -1
print("[문제 6]: n = -1 -> ", "영" if n == 0 else "0 아님","\n")


# [문제 7]
# 어떤 수 n이 10보다 크면 n을 그대로, 10 이하이면 n * 2를 반환하는
# 조건부 표현식을 작성하세요.

#   n = 15  → 15
#   n = 4   → 8
#   n = 10  → 20

n = 15
print("[문제 7]: n = 15 -> ", n if n > 10 else n * 2,"\n")

n = 4 
print("[문제 7]: n = 4 -> ", n if n > 10 else n * 2,"\n")

n = 10
print("[문제 7]: n = 10 -> ", n if n > 10 else n * 2,"\n")


# [문제 8]
# 변수 age가 18 이상이면 "성인", 미만이면 "미성년자"를 반환하는
# 조건부 표현식을 작성하세요.

#   age = 20  → "성인"
#   age = 15  → "미성년자"
#   age = 18  → "성인"

age = 20
print("[문제 8]: age = 20 -> ", "성인" if age >= 18 else "미성년자","\n")

age = 15
print("[문제 8]: age = 15 -> ", "성인" if age >= 18 else "미성년자","\n")

age = 18
print("[문제 8]: age = 18 -> ", "성인" if age >= 18 else "미성년자","\n")


# [문제 9]
# 리스트 items가 비어 있으면 "목록이 비었습니다",
# 비어 있지 않으면 items의 첫 번째 원소를 반환하는
# 조건부 표현식을 작성하세요.

#   items = [10, 20, 30]  → 10
#   items = []              → "목록이 비었습니다"

items = [10, 20, 30]
print("[문제 9]: items = [10, 20, 30] -> ", items[0] if len(items) else "목록이 비었습니다.","\n")

items = []
print("[문제 9]: items = [] -> ", items[0] if len(items) else "목록이 비었습니다.","\n")


# [문제 10]
# 두 문자열 s1, s2를 비교하여 같으면 "동일", 다르면 "다름"을 반환하는
# 조건부 표현식을 작성하세요.

#   s1, s2 = "python", "python"  → "동일"
#   s1, s2 = "hello", "world"      → "다름"

s1, s2 = "python", "python" 
print("[문제 10]: s1, s2 = python, python -> ", "동일" if s1 == s2 else "다름","\n")


s1, s2 = "hello", "world" 
print("[문제 10]: s1, s2 = hello, world  -> ", "동일" if s1 == s2 else "다름","\n")
# =======================