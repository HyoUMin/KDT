## ---------------------------------------------------------------------
## 파일 입출력 
## ---------------------------------------------------------------------
## 파일 입출력 with as 구문 -> 파일 close() 자동처리
## ------------------------------------------------------------------
## 전역 변수 설정
file_path = './my_data2.txt'

with open(file_path, mode = "r", encoding = "utf8") as F:
    all_data = F.read()
print(f"첫 번째: {all_data}\n")


with open(file_path, mode = "w", encoding = "utf8") as F:
    F.write("Good")