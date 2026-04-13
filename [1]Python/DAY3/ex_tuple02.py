# >>> 컨테이너 자료형 튜플
# Read Only라서 메서드가 몇 개 없음.

# >>> 튜플 index

a1 = ("hello", 1, 2, 1, 2, {"name" : "홍길동"}, [1, 2])
idx = a1.index("hello")
print("hello 인덱스: ", idx)
print()


if "hello" in a1:
    idx = a1.index("hello")
    print("hello 인덱스: ", idx)
print()

# >>> 튜플 count
cnt = a1.count(1)
print("1의 개수: ", cnt)
print()