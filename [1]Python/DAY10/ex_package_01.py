# >>> urllib 표준 패키지
# ===== ===== ===== ===== =====
# 웹 url 주소를 가지고 다양한 기능의 함수, 클래스 제공 모듈들
# 요청 관련 모듈 urliib.request
# url 분석 모듈 urllib.parse
# url 에러 모듈 urllib.error
# 크롤링 분석 모듈 urllib.robotparser
# ===== ===== ===== ===== =====

import urllib.request as req       # urllib.request 모듈 모두 가져오기
from urllib.request import urlopen # urlopen 함수만 가져오기

# URL에 해당하는 데이터를 저장 1
IMG_URL = R"https://mml.pstatic.net/www/mobile/edit/20260415_1095/upload_1776219728004Dd0i4.gif"
ret1, ret2 = req.urlretrieve(IMG_URL, "../DAY10/naver.jpg")

print(f'ret1 -> {ret1}') # 생성 파일 경로
print(f'ret2 -> {ret2}') # 웹의 응답 결과

# URL에 해당하는 데이터를 저장 2
retobj = urlopen(IMG_URL)
print(f"웹의 응답 결과 retobj -> {retobj}")

