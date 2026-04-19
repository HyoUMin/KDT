# =========================================================================


# >>> 파일 확장자에 따라 파일 분류하기
# >>> 이미지 파일: jpg, png, jpeg, bmp
# >>> 텍스트 파일: txt, hwp, word
# >>> 기타 파일: 이미지, 텍스트 확장자를 제외한 나머지


# =========================================================================


filename = "cat.jpg"

# 패킹으로 인덱스 접근
name1 = filename.split(".")[0]  
ext1 = filename.split(".")[1]
print(name1, ext1, "\n")


# 언패킹으로 인덱스 접근
name2, ext2 = filename.split(".")  
print(name2, ext2, "\n")


# 언패킹으로 인덱스 접근 
_, ext3 = filename.split(".")  
print(_, ext2, "\n")


# =================================================================================


# >>> 확장자에 따른 파일 종류 출력 1번 방법: if-elif문 활용

filename1 = "dog.csv"
_, ext1 = filename1.split(".")

if ext1 == "jpg" or ext1 == "jpeg" or ext1 == "png" or ext1 == "bmp":
    print(f"{filename1}: 이미지 파일\n")

elif ext1 == "hwp" or ext1 == "txt" or ext1 == "word":
    print(f"{filename1}: 텍스트 파일\n")

else:
    print(f"{filename1}: 기타 파일\n")


# ----------------------------------------------------------------------------------------------------------------------


# >>> 확장자에 따른 파일 종류 출력 1-1번 방법: if-elif문 + 멤버 연산자 

filename1 = "wolf.csv"
_, ext1 = filename1.split(".")

if ext1 in ["jpg", "jpeg", "png", "bmp"]:
    print(f"{filename1}: 이미지 파일\n")

elif ext1 in ["hwp", "txt", "word"]:
    print(f"{filename1}: 텍스트 파일\n")

else:
    print(f"{filename1}: 기타 파일\n")


# ----------------------------------------------------------------------------------


# >>> 확장자에 따른 파일 종류 출력 2번 방법: ==와 != 활용
filename2 = "cow.csv"
_, ext2 = filename2.split(".")

if ext2 == "jpg" or ext2 == "jpeg" or ext2 == "png" or ext2 == "bmp":
    print(f"{filename2}: 이미지 파일\n")

if ext2 == "hwp" or ext2 == "txt" or ext2 == "word":
    print(f"{filename2}: 텍스트 파일\n")

if ext2 != "jpg" or ext2 != "jpeg" and ext2 != "png" and ext2 != "bmp" and ext2 != "hwp" and ext2 != "txt" and ext2 != "word":
    print(f"{filename2}: 기타 파일\n")


# -----------------------------------------------------------------------------------------


# >>> 확장자에 따른 파일 종류 출력 3번 방법: 멤버 연산자 활용

filename3 = "duck.csv"
_, ext3 = filename3.split(".")

if ext3 in ["jpg", "jpeg", "png", "bmp"]:
    print(f"{filename3}: 이미지 파일\n")

if ext3 in ["hwp", "txt", "word"]:
    print(f"{filename3}: 텍스트 파일\n")

if ext3 not in ["jpg", "jpeg", "png", "bmp", "hwp", "txt", "word"]:
    print(f"{filename3}: 기타 파일\n")


