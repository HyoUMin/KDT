# >>> 파이썬 표준 패키지
# ===== ===== ===== ===== =====
# 날짜/시간 모듈들
# date 모듈
# time 모듈
# datetime 모듈
# ===== ===== ===== ===== =====

import datetime, time

# 현재 날짜/시간
print(f"현재 날짜 시간: {datetime.datetime.now()}\n")
print(f"현재 날짜 시간: {datetime.datetime.today()}\n")

current = datetime.datetime.now()
print(f"year: {current.year}년 month: {current.year}월 day: {current.day}일\n")
print(f"hour: {current.hour}시 minute: {current.minute}분 second: {current.second}초\n")

d_day = datetime.datetime(2026, 12, 31, hour = 15)
print(d_day)


print(f"현재 시간: {time.time()}\n")
print(f"현재 시간: {time.ctime(time.time())}\n")

current = time.ctime(time.time())
print(current, type(current), '\n')