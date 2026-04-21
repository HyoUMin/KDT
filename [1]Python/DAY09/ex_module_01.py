# 모듈: 특정 목적의 함수, 변수, 클래스로 구성된 py파일
# 표준 모듈: 파이썬에서 기본제공
# 사용자 정의 모듈: 개인이 만든 것
# 써드파티션 모듈: 기업, 연구소, 개인이 만든 것 -> 설차 필수
# import 모듈명 as 별칭 -> 모듈이름이 너무 길때 별칭으로 사용함.
# 모듈명.변수명 또는 모듈명.함수명() 또는 모듈명.클래스명()
import math as m

print(m.pi)
print(m.inf)
print(m.factorial(5))
print(m.pow(2, 3))


# from 모듈명 import * 로 사용시 모듈 내 모든 것을 가지고 오고, 모듈명은 필요없음.
# from math import pow as p
# print(p(2,3))

# pow이름으로 사용자 함수로 만들 경우 우선순위는 사용자 함수임.
# 가능하면 함수명을 다르게 할 것

# from math import *
# print(pow(2,3))