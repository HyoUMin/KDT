# ===========================================================
# >>> CH.32
# ===========================================================

# >>> 32.2 람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7,  8, 9, 10]
print(list(map(lambda x:str(x) if x % 3 == 0 else x, a)), "\n")


# >>> 32.2.2 map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 3, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b)), "\n")


# >>> 32.2.3 filter 사용하기
a = [8, 3, 2,10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x: x > 5 and x < 10,  a)), "\n")


# >>> 퀴즈 1.값 3개를 매개변수로 받은 뒤 매개변수를 모두 곱해서 반환하는 람다 표현식으로 올바른 것을 모두 고르세요.
# d lambda a, b, c: a * b * c


# >>> 퀴즈 2. 람다표현식 자체를 호출하는 방법으로 올바른 것을 모두 고르세요.
# b (lambda a: a + 1)(10)


# >>> 퀴즈 3. 리스트 a 요소 중 7로 끝나는 숫자만 다시 리스트로 만드는 방법으로 올바른 것을 고르세요.
# c list(filter(lambda x: x % 10 == 7, a)


# >>> 32.4 연습 문제: 이미지 파일만 가져오기
files = ["font", "1.png", "10.jpg", "11.gif", "2.jpg", "3.png", "table.xslx", "spec.docx"]
print(list(filter(lambda x: x.find(".jpg") != -1 or x.find(".png") != -1, files)), "\n")


# >>> 32.5 심사 문제: 파일 이름을 한꺼번에 바꾸기
files = input().split()
print(list(map(lambda x: f"{int(x.split('.')[0]):03d}.{x.split('.')[1]}", files)), "\n")


# ===========================================================
# >>> 33.1
# ===========================================================

# >>> 33.1.1 함수 안에서 전역 변수 변경하기
x = 10
def foo():
    x = 20
    print(x)

foo()
print(x, "\n")


# >>> 33.1.1 함수 안에서 전역 변수 변경하기

x = 10
def foo():
    global x
    x = 20
    print(x)

foo()
print(x, "\n")


# ===========================================================
# >>> 수업 예제 복슴
# ===========================================================
## --------------------
## 8. sorted의 key로 사용
## --------------------
words = ["banana", "kiwi", "apple", "grape"]
result = sorted(words, key=lambda x: len(x))
print(result)   # ['kiwi', 'apple', 'grape', 'banana']

## --------------------
## 9. 딕셔너리 값 기준 정렬
## --------------------
data = {"a": 3, "b": 1, "c": 2}
result = sorted(data.items(), key=lambda item: item[1])
print(result)   # [('b', 1), ('c', 2), ('a', 3)]



## =====================================================================
##                              복습  &  테스트
##                                                          2026-04-20
## ===================================================================== 
## [문제] 4칙 연산 계산기를 구현하세요.
## -> 기능 : 숫자 덧셈, 뺄셈, 곱셈, 나눗셈
## -> 조건 
##   ① 기능은 함수화
##   ② 2개 숫자 입력 받기
##   ③ 연산자 입력 받기
##   ④ x, X 입력 시 종료
## ===================================================================== 

def calculator(n1, n2, but_):
    if but_ == '+':
        return n1 + n2
    elif but_ == '-':
        return n1 - n2
    elif but_ == '*':
        return n1 * n2
    elif but_ == '/':
        if n2 == 0:
            return "은 잘못된 수식입니다. 0으로 나눌 수 없습니다."
        else:
            return n1 / n2

def checknum(n):
    if n.count('.') > 0:
        return float(n)
    else:
        return int(n)

while True:
    num1 = input("첫 번째 숫자를 입력하세요: ").strip()

    if not num1:
        print("입력되지 않았습니다. 다시 입력하세요.")
        continue

    if num1.lower() == 'x':
            print("계산을 종료합니다.")
            break
    
    if not num1.lstrip('-').replace('.', '', 1).isdigit():
        print("숫자가 입력되지 않았습니다.")
        continue

    num2 = input("두 번째 숫자를 입력하세요: ").strip()
    
    if not num2:
        print("입력되지 않았습니다. 다시 입력하세요.")
        continue

    if num2.lower() == 'x':
            print("계산을 종료합니다.")
            break
    
    if not num2.lstrip('-').replace('.', '', 1).isdigit():
        print("숫자가 입력되지 않았습니다.")
        continue           
                
    button = input("사칙 연산 기호를 입력하세요: ").strip()
    
    if not button:
        print("입력되지 않았습니다. 다시 입력하세요.")
        continue

    if button.lower() == 'x':
            print("계산을 종료합니다.")
            break
    
    if button not in ['+', '-', '*', '/']:
        print("잘못된 기호를 입력했습니다. 다시 입력하세요.")
        continue     

    num1 = checknum(num1)
    num2 = checknum(num2)
    result = calculator(num1, num2, button)
    print(f"{num1} {button} {num2} = {result}")       
                