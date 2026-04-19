# ===========================================================
# >>> CH.12
# ===========================================================

# >>> 퀴즈 1. 딕셔너리를 만드는 방법으로 올바르지 않은 것은?
# b x = dict('a'=10,'b'=20)


# >>> 퀴즈 2. x = {10: "hello", "world": 30}에서 키 10의 값을 출력하는 방법으로 올바른 것은?
x = {10: "hello", "world": 30}
# e
print(x[10],"\n")


# >>> 퀴즈 3. 출력 결과로 올바른 것은? 
# c 1500 2000


# 퀴즈 4. print(len({10: 0, 20: 1, 30: 2, 40: 3, 50: 4, 60:7}))의 출력 결과로 올바른 것은?
# d 6


# 12.4 연습 문제: 딕셔너리에 게임 캐릭터 능력치 저장하기.
camille = {
    "health": 575.6,
    "health_regen": 1.7,
    "mana": 338.8,
    "mana_regen":1.63,
    "melee":125,
    "attack_speed": 0.625,
    "armor": 26,
    "magic_resistance": 32.1,
    "movement_speed": 340
}

print(camille["health"])
print(camille["movement_speed"])
print()


# >>> 12.5 심사 문제: 딕셔너리에 게임 캐릭터 능력치 저장하기

keys = input().split()
values = input().split()

camille = {}

for i in range(len(keys)):
    for j in range(len(values)):
        camille1 = {keys[i]:float(values[j])}
    camille.update(camille1)

print(camille)


# ===========================================================
# >>> CH.24
# ===========================================================

# >>> 24.1.2 문자 바꾸기
table = str.maketrans("aeiou", "12345")
print("apple".translate(table), "\n")


# >>> 24.1.3 문자열 분리하기
print("apple pear grape".split())
print("apple##pear##grape".split('##'), "\n") 


# >>> 24.1.4 구분자 문자열고 문자열 리스트 연결하기
print(" ".join(["apple", "pear", "grape"]))
print("##".join(["apple", "pear", "grape"]), "\n")


# >>> 24.1.13 ~ 14 문자열 좌, 우 정렬하기
print("Python".ljust(10))
print("Python".rjust(10), "\n")


# >>> 문자열 완쪽에 0 채우기
print("35".zfill(4))
print("3.5".zfill(6))
print("hello".zfill(10),"\n")


# >>> 서식 지정자로 문자열 정렬하기
print("%10s" % "Python","\n")


# 퀴즈 1. 문자열 메서드에 대한 설명으로 잘못된 것을 모두 고르세요.
# a count는 문자열의 전체 문자 개수를 구한다
# e index는 문자열의 오른쪽에서부터 문자열을 찾아서 인덱스를 반환한다.


# >>> 퀴즈 2. 출력결과를 고르세요. 
print("Python".lower().replace("on", "ON").ljust(10),"\n")
# d 'pythON    '


# >>> 퀴즈 3. 문자열 "Hello, Python 3.6"을 만드는 방법 중 올바른 것을 모두 고르세요.
# b "%s, %s 3.6" % ("Hello, "Python")
# d "{hello}, {language} 3.6".format(hello = "Hello", language = "Python")



# >>> 퀴즈 4. '   1675.3000'을 만드는 방법으로 올바른 것을 모두 고르세요.
# c "{0:>12.4f}".format(1675.3)
# d "{: >12.4f}".format(1675.3)


# >>> 24.4 연습 문제: 파일 경로에서 파일명만 가져오기
path = R"C:\Users\KDT38\Desktop\KDT_14\[0]Work\work_0414.py"
x = path.split("\\")
print(x[-1],"\n")


# # >>> 24.5 심사 문제: 특정 단어 개수 세기
str_ = input()
print()

str_list = str_.replace(".", " ").replace(",", " ").split()
print(str_list)
print()

print(str_list.count("the"))


# >>> 24.6 심사 문제: 높은 가격 순으로 출력하기
money = input()
money_list = money.split(";")
print(money_list,"\n")
new_list = []
for i in range(len(money_list)):
    new_list.append(int(money_list[i]))
    new_list.sort(reverse=True)

for j in range(len(new_list)):
    print(f"{new_list[j]:>9,}")
 
#  51900;83000;158000;367500;250000;59200;128500;1304000