
# >>> dict 멤버연산자 사용하기. 단, 키만 가능. 값은 확인 못함.
scores_dict1 = {"국어": 90, "수학": 88, "영어": 87, "화학": 78, "지구과학": 97, "한국사":93}
print(f" 타입: {type(scores_dict1)}   원소 개수 {len(scores_dict1)}   데이터: {scores_dict1}\n")

scores_dict2 = {"물리": 90, "화학": 88, "한국지리": 83}
print(f" 타입: {type(scores_dict2)}   원소 개수 {len(scores_dict2)}   데이터: {scores_dict2}")


print(f"{'물리' in scores_dict1}")
print(f"{'물리' in scores_dict2}")
