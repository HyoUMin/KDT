# ===========================================================
# >>> CH.34
# ===========================================================

# >>> 34.2 속성 사용하기
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()    
print()


# >>> 34.2.2  인스턴스를 만들 때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    

print('이름:', maria.name)      
print('나이:', maria.age)       
print('주소:', maria.address)
print()


# >>> 34.3 비공개 속성 사용하기
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet 

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
print()


# >>> 퀴즈 1.다음 클래스의 greeting 메서드를 호출하기 위한 방법으로 올바른 것을 고르세요
class Person:
    def greeting(self):
        print("Hello")
# d. maria = Person()
#    maria.greeting()
print()

# >>> 퀴즈 2. 클래스로 인수 턴스를 만들 때 호출되는 메서드는 무엇인가요?
# __init__


# >>> 퀴즈 3. 클래스에서 다른 메서드를 만들었을 때 인스턴스 속성 name에 접근하기 위한 방법으로 올바른 것을 고르세요.
class Person:
    def _init__(self, name):
        self.name = name
# e. self.name


# >>> 퀴즈 4. 클래스의 메서드 def __init__(self):에서 속성을 만들려고 합니다. 다음 중 비공개 속성을 고르세요
# c. self.__name


# >>> 34.5 연습 문제: 게임 캐릭터 클래스 만들기
class Knight: 
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor  
    def slash(self):
        print('베기')

x = Knight(health = 542.4, mana = 210.3, armor = 38)
print(x.health, x.mana, x.armor)
x.slash()
print()


# >>> 34.6 심사 문제: 게임 캐릭터 클래스 만들기
class Annie:
    # 1. 생성자에서 체력, 마나, 주문력을 초기화합니다.
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    # 2. 티버의 피해량을 계산하여 출력하는 메서드를 만듭니다.
    def tibbers(self):
        # 공식: AP * 0.65 + 400
        damage = self.ability_power * 0.65 + 400
        print(f'티버: 피해량 {damage}')

health, mana, ability_power = map(float, input().split())
x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()
print()


# ===========================================================
# >>> CH.35
# ===========================================================
# >>> 35.1.1  클래스 속성 사용하기
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
print()


# >>> 35.1.2  인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
print()


# >>>  35.2 정적 메서드 사용하기
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20)    
Calc.mul(10, 20)   
print()


# >>> 35.3 클래스 메서드 사용하기
class Person:
    count = 0   

    def __init__(self):
        Person.count += 1    

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))  

james = Person()
maria = Person()

Person.print_count()
print()


# >>> 퀴즈 1. 다음 중 클래스 바깥에서 클래스 속성 x에 접근하는 방법으로 올바른 것을 고르세요,
class Person: 
    x = {}
# a. Person.x 


# >>> 퀴즈 2. 다음 중 정적 메서드로 올바른 것을 고르세요. 
# c. @staticmethod 
#    def div(a, b):
#        print(a /b)


# >>> 퀴즈 3. 다음 중 클래스 메서드에 대한 설명으로 잘못된 것을 고르세요.
# c. 클래스 메서드의 첫 번째 매개변수는 self이며 현재 인스턴스가 들어온다.
# e. 클래스 메서드는 위에 @staticmethod를 붙여서 만든다.


# >>> 35.5 연습 문제: 날짜 클래스 만들기
class Date:
    @staticmethod 
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

print()


# >>> 35.6 심사 문제: 시간 클래스 만들기
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second 

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return 0 <= hour <= 24 and 0 <= minute <= 59 and 0 <= second <= 60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)


time_string = input()

if Time.is_time_valid(time_string):
    t= Time.from_string(time_string)
    print(t.hour, t.minute, t.second) 
else: 
    print('잘못된 시간 형식입니다.')