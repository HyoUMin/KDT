## ---------------------------------------------------------------------
## 파일 입출력 
## ---------------------------------------------------------------------
## 동작 프로세스
## 1) 파일 열기 ---- 쓰기 모드, 인코딩 방식 설정 체크
## 2) 파일 쓰기
## 3) 파일 닫기
## ------------------------------------------------------------------
## 전역 변수 설정
file_path = './my_data2.txt'

## 파일 쓰기 - 1: x모드
## exist
## 존재하는 파일이면 에러. 반드시 새로운 파일 생성해서 쓰기
## 1) 열기 - open()
f = open(file_path, mode = "rt", encoding = "utf8")


## 파일들 속성 확인
print(f"f.closed: {f.closed}")
print(f"f.name: {f.name}")
print(f"f.mode: {f.mode}")


## 2) 읽기 - read, read(n), readline(), readlines()
all_data = f.read()
print(f"첫 번째: {all_data}\n")

## 파일 위치를 시작위치로 이동  -  seek()
## 텍스트일 때는 0에서만 동작함.
pos = f.seek(0)
print(f"pos: {pos}")
all_data = f.read()
print(f"두 번째: {all_data}\n")

cur_pos = f.tell()
print(f"cur_pos: {cur_pos}")

## 3) 닫기
f.close()


