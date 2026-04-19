# ===========================================================
# >>> CH.25
# ===========================================================

# >>> 25.2 반복문으로 딕셔너리의 키 값 쌍을 모두 출력하기.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end = " ")
print("\n")

for k, v in x.items():
    print(k, v)
print()


# >>> 25.4 딕셔너리 안에 딕셔너리 사용하기.
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'],"\n")


# >>> 25.5.1 중첩 딕셔너리의 할당과 복사
x = {'a': {"python": "2.7"}, 'b': {"pyhton": "3.6"}}
y = x.copy()
y['a']["python"] = '2.7.15'
print(x)
print(y)
print()

import copy
x = {'a': {"python": "2.7"}, 'b': {"pyhton": "3.6"}}
y = copy.deepcopy(x)
y['a']["python"] = '2.7.15'
print(x)
print(y)
print()


# >>> 퀴즈 1. 딕셔너리 x에서 키 "python"과 해당하는 값을 삭제하는 방법으로 올바른 것은?
x = {"python": 100}
x.pop("python", 100) # c
print(x)

x = {"python": 100}
del x["python"] # e
print(x)
print()


# >>> 퀴즈 2. 딕셔너리의 메서드에 대한 설명으로 올바르지 않은 것은?
# b setdefault는 키만 지정하면 값은 0으로 지정한다.
# c keys는 딕셔너리의 키-값 쌍을 모두 가져온다.


# >>> 퀴즈 3. 반복문으로 딕셔너리 x의 모든 키를 출력하는 방법으로 올바른 것은?
x = {"python": 100}

for key in x:
    print(key) # b
print()

for key in x.keys():
    print(key) # c
print()

for key, value in x.items():
    print(key) # e
print()


# >>> 퀴즈 5. satellites에 접근하는 방법 중 올바른 것을 고르세요.
terrestrial_planet = {
    'Earth': {
        'physical_ characteristics': {
            'mean_radius': 6371.0,
            'mass': 5.97219E+24 
        },
        'orbital_characteristics': {
        'orbital_period': 365.25641,
        'satellites': 1 
        }
    }, 

    'Mars': {
        'physical_characteristics': {
            'mean_radius': 3389.5,
            'mass': 6.4185E+23
            }
        }, 
        'orbital_characteristics': {
            'orbital_period': 686.9600,
            'satellites': 2
            }
}

# d
print(terrestrial_planet['Earth']['orbital_characteristics']['satellites'], "\n")


# >>> 퀴즈 6. 실행 결과로 올바른 것을 고르세요.

x = {'python': {'version': '2.7'}, 'script': {'name': 'hello.py'}}
a = x           
b = x.copy()    
c = copy.deepcopy(x) 
x['python']['version'] = '3.6'
print(a['python']['version'], b['python']['version'], c['python']['version'], "\n")

# c 3.6, 3.6, 2.7


# >>> 25.7 연습 문제: 평균 점수 구하기
maria = {"korean": 94, "english": 91, "mathematics": 89, "science": 83}
avg = sum(maria.values()) / len(maria)
print(avg, "\n")


# >>> 25.8 심사 문제: 딕셔너리에서 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x.pop('delta', None)

for v in list(x):
    if x[v] == 30:
        del x[v]
print(x)


# ===========================================================
# >>> CH.26
# ===========================================================

# >>> 26.2 집합 연산 사용하기
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = set.union(a, b)
print(c,"\n")

c = set.intersection(a, b)
print(c,"\n")

c = set.difference(a, b)
print(c,"\n")

c = set.symmetric_difference(a, b)
print(c,"\n")

a = {1, 2, 3, 4}
c = a.update({5})
print(c,"\n")

a = {1, 2, 3, 4}
c = a.intersection_update({0, 1, 2, 3, 4})
print(c,"\n")

a = {1, 2, 3, 4}
c = a.difference_update({3})
print(c,"\n")

a = {1, 2, 3, 4}
c = a.symmetric_difference_update({3, 4, 5, 6})
print(c,"\n")

a = {1, 2, 3, 4}
c = a.issubset({1, 2, 3, 4, 5})
print(c,"\n")

a = {1, 2, 3, 4}
c = a.issuperset({1, 2, 3, 4})
print(c,"\n")


a = {1, 2, 3, 4}
c = a.isdisjoint({5, 6, 7, 8})
print(c,"\n")


# >>> 퀴즈 1.세트를 만드는 방법으로 올바르지 않은 것을 고르세요.
# b a = {}


# >>> 퀴즈 2. 세트 a = {1, 2, 3, 4}와 세트 b = {3, 4, 5}가 있을 때, 집합 연산이 잘못된 것을 모두 고르세요.
# b a ^ b는 {1, 3, 5}  
# e set.difference(b, a)는 {4}


# >>> 퀴즈 3. 부분 집합, 상위 집합에 대한 설명으로 잘못된 것을 모두 고르세요.
# b 진부분 집합은 <와 issubset으로 구할 수 있고, 두 세트가 다를 때 참이다.
# d 진상위 집합은 >로 구할 수 있고, 두 세트가 같은 때 참이다.


# >>> 퀴즈 4. 세트 메서드에 대한 설명으로 올바른 것을 모두 고르세요.
# a intersection_update는 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장한다.
# b set.symmetric_difference는 두 세트의 대칭차집합을 구한다.
# c isdisjoint는 현재 세트가 다른 세트와 겹치지 않는지 확인한다.


# >>> 퀴즈 5. 메서드와 연산자의 기능이 잘못 짝지어진 것을 고르세요. 
# c symmetric_difference_update는 |=과 같다.
# d issuperset은 |과 같다.


# >>> 26.8 연습 문제: 공배수 구하기
num1, num2 = map(int, input().split())

a = set()
for i in range(1, num1 + 1):
    if num1 % i == 0:
        a.add(i)

b = set()
for i in range(1, num2 + 1):
    if num2 % i == 0:
        b.add(i)


divisor = a & b
result = 0

if  type(divisor) == set:
    result = sum(divisor)

print(result)

