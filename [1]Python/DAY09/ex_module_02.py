# 사용자 모듈 사용하기
from my_module import *

print(add(3, 2))
print(mul(3, 2))


# 다른 폴더에 있는 모듈 사용하기
import sys
sys.path.append(R"C:\Users\KDT38\Desktop\KDT_14\[1]Python\DAY07")

import ex_function_04 as ef
print(f"미술과 무용 -> {ef.get_grade(미술 = 100, 무용 = 90)}")

