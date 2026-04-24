## =============================================
##          예외처리 (Exception Handling)
## 
## -> 문법 오류가 아닌 실행 시 발생되는 오류 처리
## =============================================
## [예시] 파일이 존재하지 않는 오류
##       FileNotFoundError: [Errno 2] No such file or directory
## =============================================
FILENAME = './infor.data'

## -----------------------
## => 오류 처리 X 
## -----------------------
# with open(FILENAME, mode='r', encoding='utf8') as F:
#     print(F.read())


## -----------------------
## => 오류 처리 O 
## 여러 개의 에러 발생 시 특정 에러만 처리하는 코드에서 나머지 에러를 처리하지 못함.
## -----------------------
# try:
#     with open(FILENAME, mode='r', encoding='utf8') as F:
#         print(F.read())
# except:
#     print("파일 처리 시 문제가 발생했습니다.")


# try:
#     with open(FILENAME, mode='r', encoding='utf8') as F:
#         print(F.read())
        
# except FileNotFoundError as e:
#     print(f"{e} : 파일 처리 시 문제가 발생했습니다.")


try:
    nums = []
    print(nums[0])
    print(3 / 0)

    with open(FILENAME, mode='r', encoding='utf8') as F:
        print(F.read())

except ZeroDivisionError as e:
    print(f"ZeroDivisionError {e} : 파일 처리 시 문제가 발생했습니다.")

except FileNotFoundError as e:
    print(f"FileNotFoundError {e} : 파일 처리 시 문제가 발생했습니다.")

except IndexError as e:
    print(f"Exception {e} : 파일 처리 시 문제가 발생했습니다.")

except Exception as e:  # 예외 처리 모두 해주는 것
    print(f"Exception {e} : 파일 처리 시 문제가 발생했습니다.")

print("------ TEST END ------")






# FILENAME = './ex_package_01.py'
# F = None

# try:
#     F = open(FILENAME, mode='r', encoding='utf8')
# except:
#     print("파일 처리 시 문제가 발생했습니다.")

# else:
#     F.read()
# finally:
#     print("언제나 실행되는 부분")
#     F.close()