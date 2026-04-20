# ===========================================================
# >>> CH.29
# ===========================================================

# >>> 퀴즈 1. 매개변수가 없는 hello 함수를 호출하는 방법으로 올바른 것은?
# c. hello()


# >>> 퀴즈 2. 두 수를 받은 뒤 곱한 결과를 반환하는 함수를 만들려고 할 때, 올바른 코드를 고르세요.
# d
def mul(a, b):
    return a * b


# >>> 퀴즈 3. 값을 3개 반환하는 함수를 만들려고 할 때, 올바른 코드를 모두 고르세요.
# a
def three():
    return 1, 2, 3

# c
def three():
    return (1, 2, 3)

# d
def three():
    return [1, 2, 3]


# >>> 29.7 연습 문제: 몫과 나머지를 구하는 함수 만들기
x = 10
y = 3

def get_quotient_reminder(a, b):
    return a // b, a % b

quotient, reminder = get_quotient_reminder(x, y)
print("몫: {0}, 나머지: {1}".format(quotient, reminder))
print()


# >>> 29.8 심사 문제: 사칙연산 함수 만들기
x, y = map(int, input().split())

def calc(a, b):
    return a + b, a - b, a * b, a / b
    
a, s, m, d = calc(x, y)
print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a, s, m, d))
print()


# ===========================================================
# >>> CH.30
# ===========================================================


# >>> 퀴즈 1. def print_numbers(a, b, c):처럼 만들었을 때, 이 함수를 호출하는 방법으로 잘못된 것을 고르세요
# d. a = [3, 7, 9]
#    print_numbers(**a)


# >>> 퀴즈 2. print_numbers(*[10, 20, 30])으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요.
# b. def print_numbers(a, b, c):
# c. def print_numbers(*args):


# >>> 퀴즈 3. personal_info(**{"name": "홍길동", "age": 30})으로 호출할 수 있는 함수로 올바른 것을 모두 고르세요.
# a. def personal_info(**kawrgs)
# c. def personal_info(name = "미공개", age = 0) 


# >>> 30.6 연습 문제: 가장 높은 점수를 구하는 함수 만들기
kor, eng, math, sci = 100, 86, 81, 91
def get_max_score(*args):
    return max(args)

max_score = get_max_score(kor, eng, math, sci)
print("높은 점수: ", max_score)

max_score = get_max_score(eng, sci)
print("높은 점수: ", max_score)
print()


# >>> 30.7 심사 문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)
            

def get_average(**kwargs):
    return sum(kwargs.values()) / len(kwargs)

min_score, max_score = get_min_max_score(korean, english, mathematics)

average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science) 

print("낮은 점수: {0:.2f}, 높은 점수: {1: .2f}, 평균 점수: {2: .2f}".format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)

average_score = get_average(english=english, science=science)

print("낮은 점수: {0:.2f}, 높은 점수: {1: .2f}, 평균 점수: {2: .2f}".format(min_score, max_score, average_score))
