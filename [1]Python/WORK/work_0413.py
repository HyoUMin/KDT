# ===========================================================
# >>> CH.9
# ===========================================================


# >>> 9.1.1 여러 줄로 된 문자열 사용하기
hello = """hello, world!
안녕하세요.
Python입니다.
"""

print(hello)


# >>> 퀴즈 1. 문자열을 표현하는 방법 중 올바른 것은?
b = "hello, world!"
d = 'hello, world!'
print(b)
print(d)


# >>> 퀴즈 2. 문자열을 여러 줄로 표현하는 방법 중 올바른 것은?
a = '''안녕하세요.
파이썬입니다.
'''
c = """안녕하세요.
파이썬입니다.
"""
print(a)
print(c)


# >>> 퀴즈 3. 문자열 안에 작은 따옴표나 큰 따옴표를 넣는 방법 중 올바른 것은?
a = 'Hello, \'Python\'' 
c = "Hello, 'Python'"
d = """"Hello", Python"""
print(a)
print(c)
print(d)


# >>> 9.3 연습 문제. 여러 줄로 된 문자열 사용하기
s = """
Python is a programming language that lets you work quickly
and
intergrate systems more efficiently.
"""
print(s)


# >>> 9.4 심사 문제. 여러 줄로 된 문자열 사용하기
s = """'Python' is a "programming language" that lets you work quickly
and
intergrate systems more efficiently.
"""
print(s)


# ===========================================================
# >>> CH.22
# ===========================================================


# >>> 22.1.2 리스트에 요소 하나 추가하기
a = [10, 20, 30]
a.append(500)
print(a, len(a))
print()


# >>> 22.1.4 리스트 확장하기
a = [10, 20, 30]
a.extend([500, 600])
print(a, len(a))
print()


# >>> 22.1.5 리스트의 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500)
print(a, len(a))
print()

a = [10, 20, 30]
a.insert(len(a), 500) # a.append(500)과 동일
print(a, len(a))
print()


# >>> 22.1.7 리스트에서 특정 인덱스의 요소 삭제하기
a = [10, 20, 30]
a.pop() # 마지막 요소 삭제
print(a, len(a))
print()

a = [10, 20, 30]
a.pop(1) # 해당 인덱스 요소 삭제. del a[1]과 동일
print(a, len(a))
print()


# >>> 22.1.8 리스트에서 특정 값을 찾아서 삭제하기
a = [10, 20, 30]
a.remove(20)
print(a, len(a))
print()

a = [10, 20, 30, 20]
a.remove(20) # 처음 찾은 값을 삭제
print(a, len(a))
print()


# >>> 22.1.9 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20)) 
print()


# >>> 22.1.10 특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20)) 
print()


# >>> 22.1.11 리스트의 순서 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)
print()


# >>> 22.1.12 리스트 요소 정렬하기
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)
print()


# >>> 22.1.13 리스트의 모든 요소 삭제하기
a = [10, 20, 30, 15, 20, 40]
a.clear() # del [:]과 동일한 의미
print(a)
print()


# >>> 22.1.14 리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a):] = [500]
print(a)
print()


# >>> 22.3.1 for 문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)
print()


# >>> 22.3.2 인덱스와 요소를 함께 출력하기.
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)
print()

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index + 1, value)
print()

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a, start = 1):
    print(index, value)
print()


# >>> 22.3.3 while 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1
print()


# >>> 22.4.1 가장 작은 수와 가장  큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)
print()

a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)
print()


# >>> 22.6 리스트에 map() 사용하기
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)
print()


# >>> 22.6.1 input().split()과 map
a = map(int, input().split())
print(a)


# >>> 퀴즈 1. 리스트 a가 있을 때, 리스트 a.append(4)와 동작이 같은 것은?
a = [1, 2]
a.insert(len(a), 40)
print(a)
print()

a = [1, 2]
a[len(a):] = [40]
print(a)
print()


# >>> 퀴즈 2. 리스트의 모든 요소를 삭제하는 메서드
a = [1, 2]
a.clear()
print(a)
print()


# >>> 퀴즈 3. 리스트  a요소를 모두 출력하는 방법으로 올바른 것은?
a = [1, 2, 3]

# a
for i in range(len(a)):
    print(a[i])

# d
i = 0
while i < len(a):
    print(a[i])
    i += 1

# e
for i in a:
    print(i)


# >>> 퀴즈 4. a에 사용할 수 없는 코드
# b a.pop()


# >>> 퀴즈 5. 리스트 [0, 1, 2, 3, 17, 18, 19]를 만드는 방법으로 올바른 것은?
# d [i for i in range(20) if i <= 3 or i >= 17]


# >>> 퀴즈 6. 실수가 들어있는 리스트 [4.7, 3.5, 2.9]의 요소를 문자열로 변환하는 방법으로 올바른 것은?
# c a = list(map(str, [4.7, 3.5, 2.9]))


# >>> 22.9 연습 문제: 리스트에서 특정 요소만 뽑아내기
a = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india"]
b = [i for i in a if len(i) == 5]
print(b)
print()


# >>> 22.10 심사 문제: 2의 거듭제곱 리스트 생성하기
a = int(input())
b = int(input())

list_ = []

for i in range(a, b + 1):
    list_.append(2 ** i)

print(list_)