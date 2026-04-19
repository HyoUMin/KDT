# ================================================================
#  Python 컨프리헨션 실습 문제집
#  List / Set / Dictionary Comprehension
# ================================================================

# ----------------------------------------------------------------
#  1. 리스트 컨프리헨션 (List Comprehension)
# ----------------------------------------------------------------
# ★ 초급 (Beginner)

# [문제 1-1]
# 1부터 20까지의 정수 중에서 짝수만 골라 리스트를 만드세요.
# 예상 출력: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

list1 = list(range(1, 21))

new_list1 = [num for num in list1 if not num % 2]

print("[1-1]: ",new_list1, "\n")

# [문제 1-2]
# 문자열 리스트 ["hello", "world", "python", "list"]에서
# 각 단어를 대문자로 변환한 새 리스트를 만드세요.
# 예상 출력: ['HELLO', 'WORLD', 'PYTHON', 'LIST']

list2 = ["hello", "world", "python", "list"]

new_list2 = [num.upper() for num in list2] 

print("[1-2]: ",new_list2, "\n")

# [문제 1-3]
# numbers = [1, 2, 3, 4, 5]일 때,
# 각 숫자의 제곱값을 담은 리스트를 만드세요.
# 예상 출력: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]

new_list3 = [num**2 for num in numbers]

print("[1-3]: ",new_list3, "\n")

# [문제 1-4]
# 문자열 "Hello, World!"에서 알파벳 소문자만 추출하여 리스트를 만드세요.
# 예상 출력: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

list4 = "Hello, World!"

new_list4 = [num for num in list(list4) if num.islower()]

print("[1-4]: ",new_list4, "\n")


# [문제 1-5]
# 0부터 9까지의 숫자 중 3의 배수(0 포함)를 담은 리스트를 만드세요.
# 예상 출력: [0, 3, 6, 9]

list5 = list(range(0, 10))

new_list5 = [num for num in list5 if not num % 3]

print("[1-5]: ",new_list5, "\n")

# ---

# ★★ 중급 (Intermediate)

# [문제 1-6]
# numbers = [3, -1, 4, -1, 5, -9, 2, -6, 5]에서
# 양수는 그대로, 음수는 0으로 바꾼 리스트를 만드세요.
# 예상 출력: [3, 0, 4, 0, 5, 0, 2, 0, 5]

numbers = [3, -1, 4, -1, 5, -9, 2, -6, 5]

new_list6 = [num if num >= 0 else 0 for num in numbers]

print("[1-6]: ", new_list6, "\n")

# [문제 1-7]
# matrix = [[1,2,3],[4,5,6],[7,8,9]] 인 2차원 리스트를
# 1차원 리스트로 평탄화(flatten)하세요.
# 예상 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

new_list7 = [num for i in matrix for num in i]

print("[1-7]: ", new_list7, "\n")

# [문제 1-8]
# words = ["apple", "banana", "cherry", "date", "elderberry"]에서
# # 글자 수가 5 이상인 단어들만 대문자로 변환하여 리스트를 만드세요.
# 예상 출력: ['APPLE', 'BANANA', 'CHERRY', 'ELDERBERRY']

words = ["apple", "banana", "cherry", "date", "elderberry"]

new_list8 = [i.upper() for i in words if len(i) >= 5]

print("[1-8]: ", new_list8, "\n")

# [문제 1-9]
# 두 리스트 a = [1,2,3]과 b = [4,5,6]에서
# a의 원소 * b의 원소 조합 중 곱이 10 이상인 경우만 모아
# (a원소, b원소, 곱) 튜플 리스트를 만드세요.
# 예상 출력: [(2, 5, 10), (2, 6, 12), (3, 4, 12), (3, 5, 15), (3, 6, 18)]

a = [1,2,3]
b = [4,5,6]
new_list9 = [(i, j, i * j) for i in a for j in b if i * j >= 10]

print("[1-9]:", new_list9, "\n")

# [문제 1-10]
# sentences = ["I love Python", "Python is fun", "I am learning"]에서
# 각 문장을 단어 단위로 분리하되, "Python"이 포함된 문장의 단어만 모아
# 하나의 리스트로 만드세요.
# 예상 출력: ['I', 'love', 'Python', 'Python', 'is', 'fun']

sentences = ["I love Python", "Python is fun", "I am learning"]

new_list10 = [word for s in sentences if "Python" in s for word in s.split()]

print("[1-10]:", new_list10, "\n")
# ---


# ----------------------------------------------------------------
#  2. 셋 컨프리헨션 (Set Comprehension)
# ----------------------------------------------------------------

# ★ 초급 (Beginner)

# [문제 2-1]
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]에서
# 중복을 제거한 값들의 집합을 셋 컨프리헨션으로 만드세요.
# 예상 출력: {1, 2, 3, 4}

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

set1 = {num for num in numbers}

print("[2-1]: ", set1, "\n")

# [문제 2-2]
# 1부터 10까지의 숫자에서 2의 배수 집합을 만드세요.
# 예상 출력: {2, 4, 6, 8, 10}

set2 = set(range(1, 11))

new_set2 = {num for num in set2 if not num % 2}

print("[2-2]: ", new_set2, "\n")

# [문제 2-3]
# 문자열 "mississippi"에서 등장하는 고유 문자들의 집합을 만드세요.
# 예상 출력: {'m', 'i', 's', 'p'}
set3 = "mississippi"

new_set3 = {num for num in set(set3)}

print("[2-3]: ", new_set3, "\n")

# [문제 2-4]
# words = ["apple","banana","cherry","apricot","blueberry"]에서
# 첫 글자만 모은 집합을 만드세요. (중복 없음)
# 예상 출력: {'a', 'b', 'c'}

words = ["apple","banana","cherry","apricot","blueberry"]


# [문제 2-5]
# numbers = [1,2,3,4,5,6,7,8,9,10]에서
# 각 숫자를 제곱한 값들의 집합을 만드세요.
# 예상 출력: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_set5 = {num ** 2 for num in set(numbers)}

print("[2-5]: ", new_set5, "\n")

# ---

# ★★ 중급 (Intermediate)

# [문제 2-6]
# 문자열 리스트 words = ["Python","python","PYTHON","Java","java","JAVA"]에서
# 모두 소문자로 변환한 뒤 중복을 제거한 집합을 만드세요.
# 예상 출력: {'python', 'java'}

words = ["Python","python","PYTHON","Java","java","JAVA"]

new_set6 = {i.lower() for i in words}

print("[2-6]: ", new_set6, "\n")

# [문제 2-7]
# a = {1,2,3,4,5}, b = {3,4,5,6,7} 일 때,
# 셋 컨프리헨션으로 두 집합 중 하나에만 속하는 원소들의 집합(대칭 차집합)을 만드세요.
# 예상 출력: {1, 2, 6, 7}
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

new_set7 = {i for i in (a | b) if i not in (a & b)}

print("[2-7]: ", new_set7, "\n")

# [문제 2-8]
# sentences = ["I love Python", "Python is great", "I enjoy coding"]에서
# 모든 문장에 등장하는 단어들을 소문자 변환 후 중복 없이 모은 집합을 만드세요.
# 예상 출력: {'i', 'love', 'python', 'is', 'great', 'enjoy', 'coding'}

sentences = ["I love Python", "Python is great", "I enjoy coding"]

new_set8 = {i.lower() for j in sentences for i in j.split()}

print("[2-8]: ", new_set8, "\n")


# [문제 2-9]
# numbers = list(range(1, 21))에서
# 3의 배수이거나 7의 배수인 숫자들의 집합을 만드세요.
# 예상 출력: {3, 6, 7, 9, 12, 14, 15, 18}

numbers = list(range(1, 21))

new_set9 = {i for i in numbers if i % 3 == 0 or i % 7 == 0}

print("[2-9]: ", new_set9, "\n")


# [문제 2-10]
# pairs = [(1,2),(2,3),(3,4),(1,3),(2,4)]에서
# 각 쌍의 합이 짝수인 경우, 그 합 값들로 집합을 만드세요.
# 예상 출력: {4, 6}

pairs = [(1,2),(2,3),(3,4),(1,3),(2,4)]

new_set10 = {i + j for i, j in pairs if (i + j) % 2 == 0 }

print("[2-10]: ", new_set10, "\n")

# ---


# ----------------------------------------------------------------
#  3. 딕셔너리 컨프리헨션 (Dictionary Comprehension)
# ----------------------------------------------------------------

# ★ 초급 (Beginner)

# [문제 3-1]
# 1부터 5까지의 숫자를 키로, 그 제곱을 값으로 하는 딕셔너리를 만드세요.
# 예상 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict1 = {key: key **2  for key in dict.fromkeys([1, 2, 3, 4, 5]).keys()}  
print("[3-1]: ", dict1, "\n")

# [문제 3-2]
# words = ["apple","banana","cherry"]에서
# 단어를 키로, 단어의 길이를 값으로 하는 딕셔너리를 만드세요.
# 예상 출력: {'apple': 5, 'banana': 6, 'cherry': 6}

words = ["apple","banana","cherry"]

dict2 = {key: len(key)  for key in dict.fromkeys(words).keys()}

print("[3-2]: ", dict2, "\n")

# [문제 3-3]
# 기존 딕셔너리 d = {'a':1, 'b':2, 'c':3}의 키와 값을 서로 뒤집은 딕셔너리를 만드세요.
# 예상 출력: {1: 'a', 2: 'b', 3: 'c'}

d = {'a':1, 'b':2, 'c':3}

dict3 = {v: k for k, v in d.items()}

print("[3-3]: ", dict3, "\n")

# [문제 3-4]
# keys = ['name','age','city'], values = ['Alice', 30, 'Seoul']을
# zip으로 묶어 딕셔너리를 만드세요.
# 예상 출력: {'name': 'Alice', 'age': 30, 'city': 'Seoul'}

keys = ['name','age','city']
values = ['Alice', 30, 'Seoul']

dict4 = {k: v for k, v in zip(keys, values)}

print("[3-4]:", dict4,"\n")

# [문제 3-5]
# 알파벳 'a'부터 'e'까지를 키로, 해당 알파벳의 ASCII 코드를 값으로 하는
# 딕셔너리를 만드세요.
# 예상 출력: {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}
dict5 = {k: ord(k)  for k in ['a','b' ,'c', 'd', 'e']}  

print("[3-5]: ", dict5, "\n")
# ---

# ★★ 중급 (Intermediate)

# [문제 3-6]
# scores = {'Alice':85, 'Bob':42, 'Carol':91, 'Dave':58, 'Eve':76}에서
# 점수가 60 이상인 학생만 포함하고, 점수에 5점을 더한 딕셔너리를 만드세요.
# 예상 출력: {'Alice': 90, 'Carol': 96, 'Eve': 81}
scores = {'Alice':85, 'Bob':42, 'Carol':91, 'Dave':58, 'Eve':76}

dict6 = {k: v + 5 for k, v in scores.items() if v >= 60}  

print("[3-6]: ", dict6, "\n")

# ---
# [문제 3-7]
# text = "hello world"에서 각 문자를 키로, 등장 횟수를 값으로 하는
# 딕셔너리를 컨프리헨션으로 만드세요. (공백 제외)
# 예상 출력: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

text = "hello world"

dict7  = {k: text.count(k) for k in text if k != " "}  

print("[3-7]: ", dict7, "\n")


# [문제 3-8]
# items = [("apple",3),("banana",5),("cherry",2),("date",8)]에서
# 수량이 4 이상인 항목만 골라 {품목: 수량} 딕셔너리를 만드세요.
# 예상 출력: {'banana': 5, 'date': 8}

items = [("apple",3),("banana",5),("cherry",2),("date",8)]

dict8  = {i: j for i, j in items if j >= 4}  

print("[3-8]: ", dict8, "\n")

# [문제 3-9]
# numbers = [1,2,3,4,5,6,7,8,9,10]에서
# 홀수는 키로 "odd", 짝수는 키로 "even"으로 분류하되,
# {숫자: "odd"/"even"} 형태의 딕셔너리를 만드세요.
# 예상 출력: {1:'odd',2:'even',3:'odd',4:'even',5:'odd',
#             6:'even',7:'odd',8:'even',9:'odd',10:'even'}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dict9 = {num: "even" if num % 2 == 0 else "odd" for num in numbers}

print("[3-9]:", dict9,"\n")

# [문제 3-10]
# two = {1:'one',2:'two',3:'three'}, three = {2:'TWO',3:'THREE',4:'FOUR'}
# 두 딕셔너리에서 공통 키만 골라 {키: (값1, 값2)} 형태의 딕셔너리를 만드세요.
# 예상 출력: {2: ('two', 'TWO'), 3: ('three', 'THREE')}

# ---

two = {1: 'one', 2: 'two', 3: 'three'}
three = {2: 'TWO', 3: 'THREE', 4: 'FOUR'}

dict10 = {k: (two[k], three[k]) for k in two.keys() & three.keys()}

print("[3-10]:", dict10, "\n")