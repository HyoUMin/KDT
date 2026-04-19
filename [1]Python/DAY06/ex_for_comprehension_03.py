# ===== ===== ===== ===== =====
# >>> for comprehension -> dict
# ===== ===== ===== ===== =====

org_dict = {"국어": 98, "수학": 56, "영어": 78, "과학": 86}
print(org_dict, "\n")


# >>> 과목별 점수를 100으로 나눈 값을 저장하는 dict


new_dict = {key:org_dict[key] / 100 for key in org_dict}
print(new_dict, "\n")

new_dict = {k: v / 100 for k, v in org_dict.items()}
print(new_dict, "\n")

# >>> 점수가 80점 이상인 과목만 저장하는 딕셔너리
new_dict = {key:org_dict[key] / 100 for key in org_dict if org_dict[key] >= 80}
print(new_dict, "\n")

new_dict = {k: v / 100 for k, v in org_dict.items() if v >= 80}
print(new_dict, "\n")

# >>> 점수가 80점 이상이면 합격 아니면 불합격 저장하는 딕셔너리
new_dict = {key: "합격" if org_dict[key] >= 80 else "불합격" for key in org_dict}
print(new_dict, "\n") 

new_dict = {
    k: "합격" if v >= 80 else
    "불합격" 
    
    for k, v in org_dict.items()
    
}
print(new_dict, "\n") 


# >>> 점수에 따라 학점 A, B, C, D, F로 저장하는 Dict
new_dict = {
    k: "A" if v >= 90 else 
    "B" if v >= 80 else 
    "C" if v >= 70 else 
    "D" if v >= 60 else 
    "F" 
            
    for k, v in org_dict.items()
}
print(new_dict, "\n")


