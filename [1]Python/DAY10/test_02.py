# ================================================
# 문제 2. 회원 추가 기능 만들기
# ------------------------------------------------
# 구현 : 회원 관리 프로그램의 회원 등록 기능.
#
# 요구사항
# -> 사용자에게 연락처, 이름, 지역, 직업, 취미 입력받기.
# -> 입력받은 정보를 users.txt 파일에 추가 저장.
# -> 이미 저장된 회원 정보는 유지되어야 함.
# -> 저장 후 "회원 등록 완료" 출력.
# -> 이미 존재하는 회원이면 "이미 등록되어 있습니다" 출력.

# 저장 형식
# -> 연락처             이름    지역    직업      취미
# -> 010-1234-5678     태권V   대구    운동선수   태권도
# ================================================


# >>> 교수님 설계
# ===== ===== ===== ===== =====
# 1. 관련 기능 폴더 및 파일명 설정
## 1-1. 폴더명: Member 
## 1-2. 파일명: users.txt'

# 2. 회원 등록 기능
## 2-1. 함수 이름: join_user
## 2-2. 매개변수: 연락처, 이름, 지역, 직업, 취미
## 2-3. 함수 기능: user.txt 파일에 계속 추가. 
## 2-4. 함수 기능: 존재하는 회원일 경우 추가 X. 
## 2-5. 함수 기능: 미존재하는 회원만 추가. 메세지 출력

# 3. 폴더 및 저장 파일 준비 기능
## 3-1. 함수 이름: create_dir_file
## 3-2. 매개변수: 생성할 폴더 또는 파일 경로
## 3-3. 함수 기능: 폴더 또는 파일 생성
## 3-4. 함수 기능: Member 폴더 생성
## 3-5. 함수 기능: users.txt 파일 첫 번째 줄에 기록
# ===== ===== ===== ===== =====


# >>> 교수님 코드
# ===== ===== ===== ===== =====
import os

MEMBER_PATH = '../MEMBER'

USER_FILE = os.path.join(MEMBER_PATH, 'users.txt')
# ----- ----- ----- ----- -----
# 함수 이름: create_dir_file
# 함수 기능: 폴더 또는 파일 생성
# 매개변수: path(생성할 폴더 또는 파일 경로), isfile = False(생성하는 것이 파일인지 폴더인지...) 
# 함수 결과: 생성 여부 True/False 반환 
# ----- ----- ----- ----- -----

def create_dir_file(path, isfile =  False):
    # 폴더 생성
    if not isfile:
        os.mkdir(path)
    else:
        # 파일 생성
        with open(USER_FILE, mode = 'x', encoding = 'utf8') as F:
            F.write(f"{'연락처':^15}{'이름':^10}{'지역':^10}{'직업':^10}{'취미':^10}")

    return os.path.exists(path)

# ----- ----- ----- ----- -----
# 함수 이름: join_user
# 함수 기능: 회원 등록 / 파일 저장
# 매개변수: phone, name, loc, job, hobby
#          phone - 중복되지 않는 데이터로써 식별자(id)
#          전화번호 형식, 숫자 구성 체크
# 함수 결과: 생성 여부 True/False 반환
# ----- ----- ----- ----- -----

def join_user(phone, name, loc, job, hobby):
    # 연락처 데이터 형식 및 구성 검사
    if phone.replace('-','').isdecimal():
        # 파일 데이터 추출

        with open(USER_FILE, 'r', encoding = 'utf8') as rF:
            all_datas = rF.read()

        # 중복 여부 체크
        if phone in all_datas:
            print(f"{phone} 이미 등록된 회원입니다.")
        else:
            # 새로운 회원으로 추가
            with open(USER_FILE, 'a', encoding = 'utf8') as F:
                wCnt = F.write(F.write(f"{'연락처':^15}{'이름':^10}{'지역':^10}{'직업':^10}{'취미':^10}"))
                print(f"{wCnt}개 데이터 저장")
    else:
        print("유효한 데이터가 아닙니다.")

create_dir_file(MEMBER_PATH)
create_dir_file(USER_FILE, True)

# ----- ----- ----- ----- -----
# 기능 테스트
# ----- ----- ----- ----- -----
# 폴더 및 파일 생성
if create_dir_file(MEMBER_PATH) and create_dir_file(USER_FILE, True):
    print("폴더 및 파일 준비 완료")

    # 등록 요청
    in_data = input("회원등록 연락처, 이름, 지역, 직업, 취미 입력: ").strip().split(',')

    if len(in_data) == 5:
        join_user(*in_data)
    else:
        print("필수 회원 정보 연락처, 이름, 지역, 직업, 취미가\n모두 입력되었는지 확인바랍니다.")

else:
    print("폴더 및 파일이 준비되지 않았습니다.")