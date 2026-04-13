## =====================================
## 컨테이너 자료형 - [2] tuple
## 다양한 자료형 데이터 여러 개를 저장 가능
## 단, 저장과 읽기만 가능함. 값을 수정하거나 지우는 것은 안됨
## =====================================

a1 = ("hello", 1, 2, 3)
a2 = "hello", 1, 2, 3
a3 = ("hello", ) # 데이터가 1개인 경우엔, 쉼표 필수
a4 = "hello",    # 데이터가 1개인 경우엔, 쉼표 필수
a5 = ("hello")   # 쉼표가 없어서 str로 저장됨. 튜플로 저장안됨.

print(f"a1: {a1}   타입: {type(a1)}")
print(f"a2: {a2}   타입: {type(a2)}")
print(f"a3: {a3}   타입: {type(a3)}")
print(f"a4: {a4}   타입: {type(a4)}")
print(f"a5: {a5}   타입: {type(a5)}")
print()


# 멤버 연산자 확인가능. 튜플 더하기, 튜플 곱하기 가능(이 때, 새로운 튜플이 새로 생기는 것임.)
new_a1 = a1 + a2
print(new_a1)
print()

new_a2 = a1 * 4
print(new_a2)
print()


print(f"10 in new_a1: {2 in new_a1}")
print(f"\"Hi\" in new_a1: {'Hi' in new_a1}")