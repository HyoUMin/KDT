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
                