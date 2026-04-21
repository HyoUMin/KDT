## ---------------------------------------------------------------------
## 경로
## - 절대경로 : 윈도우 os 관점에서 드라이브(C, D, ...) 
##   [예] C:\Users\kwon\Desktop\PYTORCH_IMAGE\data\flower.jpg
## - 절대경로 : 리눅스 관점에서 루트(/)
## - 상대경로 : 현재 파일이 있는 위치를 기준으로 경로/파일 위치 설정
##  특별한 의미를 가진 ., .. 기호룰 사용함. 
##  [예] ../data/flower.jpg -> flower.jpg 앞에 생략해도 가능.
## ---------------------------------------------------------------------
##  파일의 경로
##  1) tmp_in.txt:  현재 파이썬 코드 파일과 동일한 폴더에 존재
##  2) tmp_out.txt: [1]PYTHON 폴더 안에 존재.
##                  현재 파이썬 코드파일과 다른 위치에 있음.     
## ------------------------------------------------------------------
## 파일 및 경로 관련 함수, 클래스 존재하는 파일: 모듈
## 모듈을 코드에 포함하기. import
import os 

## 전역 변수 파일 경로 설정

file_path_abs1 = R"C:\Users\KDT38\Desktop\KDT_14\[1]Python\DAY09\tmp_in.txt"
## 코드 파일과 같은 위치에 존재 즉, 현재 위치를 의미함. -> 기호 ./
##  file_path_re1 = "./tmp_in.txt"
file_path_re1 = "tmp_in.txt" # 생략해도 현재 코드 경로를 자동으로 찾아감.


file_path_abs2 = R"C:\Users\KDT38\Desktop\KDT_14\[1]Python\tmp_out.txt"
## 현재 코드 파일 경로보다 한 단계 위에 존재한다는 의미 -> 기호 ../
file_path_re2 = "../tmp_out.txt"

## 파일 존재 여부 검사
## -------------------------------------------------------------------------------
## os 모듈 함수 사용하기
print(f"[1] 절대경로: {os.path.exists(file_path_abs1)}\n")
print(f"[2] 상대경로: {os.path.exists(file_path_re1)}\n")
print(f"[3] 절대경로: {os.path.exists(file_path_abs2)}\n")
print(f"[4] 상대경로: {os.path.exists(file_path_re2)}\n")


## [실습] check.py 파일의 절대경로와 상대경로를 출력하기

file_abs = R"C:\Users\KDT38\Desktop\KDT_14\[1]Python\DAY01\check.py"
file_re = "../DAY01/check.py"

print(f"[1] 절대경로: {os.path.exists(file_abs)}\n")
print(f"[2] 상대경로: {os.path.exists(file_re)}\n")