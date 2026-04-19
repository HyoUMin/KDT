# >>> if 조건문:
# >>> ----실행코드
# >>> else:
# >>> ----실행코드

msg = ""
if  len(msg):
    print("Good")
else:
    print("입력된 내용이 없습니다.")



name = input("이름 입력: ").strip()
if len(name):
    name = name.replace(" ", "")
    if name.isalpha():
        print(name)
    else:
        print("올바른 입력이 아닙니다.")    
else:
    print("올바른 입력이 아닙니다.")