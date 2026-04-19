# >>> bool 자료형
# >>> 정수 0, 1과 논리 0, 1의 모호성을 해결하기 위한 자료형 True/False

data1 = False
data2 = True
data3 = bool(False)

print(data1, type(data1))
print(data2, type(data2))
print(data3, type(data3))

# >>> bool 자료형과 다른 자료형 사이의 변환
# >>> bool(data) : 해당 데이터를 bool형태로 변환

a = bool("A")
print(a)

b = bool(-3)
print(b)

c = bool(0)
print(c)

c = int(c)
print(c)

d = bool(" ")
print(d)

e = bool("") # 원소 개수가 없으므로 False임.
print(e) 

f = bool([[]])
print(f)

g = bool([])
print(g)