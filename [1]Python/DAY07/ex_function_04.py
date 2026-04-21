## =================================================
## 함수의 매개변수/파라미터 
##
## -> 함수 코드 실행 시에 필요판 데이터를 전달 받는 변수
## -> 함수마다 개수가 다름 또는 없는 경우도 있음
#
## =================================================
## 함수기능 : 학생의 학점을 출력해주는 기능. 학생마다 과목개수와 과목이 다름
## 함수이름 : get_grade
## 매개변수 : **score
## 함수결과 : grade
## =================================================

def get_grade(**score): # 딕셔너리로 받음
    # print("키워드 파라미터: ", type(score), "\n")
    grade = 0
    for num in score.values():
        grade += num 
    
    avg = (grade / len(score)) if len(score) else 0
    
    return avg

# 해당 파일이 다른 파일에 import될 때는 아래 코드는 실행되지 않음.
if __name__ == '__main__':
    print(get_grade(), type(get_grade()), "\n")
    print(get_grade(kor=90, eng=87), "\n")
    print(get_grade(sci = 89, art = 80, dance = 77), "\n")
    print(f"매직/스페셜 변수 __name__: {__name__}")
