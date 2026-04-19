# >>> dict 메서드 사용하기

scores_dict1 = {"국어": 90, "수학": 88, "영어": 87, "화학": 78, "물리": 100, "생물":93}

# >>> keys() -> dict_keys 타입 반환
keys = scores_dict1.keys()
print(f"키 반환: {keys}\n")

# >>> values() -> dict_values 타입 반환
values = scores_dict1.values()
print(f"키 반환: {values}\n")

# >>> items() -> dict_items 타입 반환
items = scores_dict1.items()
print(f"키 반환: {items}\n")

# >>> get(키, 반환값) -> 기본값: 키가 존재하지 않을 시 반환할 값
get1 = scores_dict1.get("국어", "NO")
print(f"키 반환: {get1}\n")


# >>> 인덱싱 방법으로 읽기 못함 -> 리스트 등 형태로 형변환 후 가능
# >>> for 반복문으로 접근은 가능함.
for v in values: print(v)
print()

for k in keys: print(k)
print()

for i in items: print(i)
print()

for k, v in items: print(f"{k}: {v:>3}")
print()
