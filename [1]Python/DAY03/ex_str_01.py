## ================================
## 기본 + 컨테이너 - [3] str 타입
## >>> 멤버 연산자 사용 가능
## ================================

# >>> 변수 없이 """ """ 또는  ''' ''' 사용시 여러 줄 주석임.

# >>> \U 유니코드 의미 문자

# >>> Raw String: 문자열 내에 이스케이프 문자를 사용하지 않음.
# >>> r"문자열" 또는 R"문자열"

data1 = "Good\nLuck\t!!"
data2= R"Good\nLuck\t!!"

print(f"data1: {data1}")
print()
print(f"data2: {data2}")


## Raw String 활용 => 경로(PATH) 관련
data_path = R"C:\Users\KDT38\Desktop\KDT_14\[1]Python\Test.txt"
print("txt 파일 경로: ", data_path)