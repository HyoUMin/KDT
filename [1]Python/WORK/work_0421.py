# ===========================================================
# >>> CH.27
# ===========================================================

# >>> 27.1.1 파일에 문자열 쓰기
file = open('hello.txt', 'w')
file.write('hello, world!')
file.close()


# >>> 27.1.2 파일에서 문자열 읽기
file = open('hello.txt', 'r')
s = file.read()
print(s, '\n')
file.close()


# >>> 27.1.3 자동으로 파일 객체 닫기
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s, '\n')


# >>> 27.2.1 반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('hello, world {0}\n'.format(i))


# >>> 27.2.2 리스트에 들어있는 문자열을 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w', encoding = 'utf8') as file:
    file.writelines(lines)


# >>> 27.2.3 파일의 내용을 한 줄씩 리스트로 가져오기
with open('hello.txt','r', encoding = 'utf8') as file:
    lines = file.readlines()
    print(lines, '\n')


# >>> 27.2.4 파일의 내용을 한 줄씩 읽기
with open('hello.txt', "r", encoding='utf8') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n')) 


# >>> 27.2.5 for문으로 파일의 내용을 줄 단위로 읽기
with open('hello.txt', 'r', encoding = 'utf8') as file:
    for line in file:
        print(line.strip('\n')) 


# >>> 퀴즈 1. 파일에 문자열을 쓸 때, 파일 열기 방법으로 올바른 것을 고르세요.
# d file = open('hello.txt', 'w')


# >>> 퀴즈 2. 파일에서 문자열을 한 줄씩 읽어서 리스트 형태로 가져오는 메소드로 올바른 것을 고르세요.
# c readlines


# >>> 퀴즈 3. pickle 모듈 문제이므로 생략합니다.


# >>> 27.5 연습 문제: 파일에서 10자 이하인 단어 개수 세기
word = ['anonymously\n', 'compatibility\n', 'dashboard\n', 'experience\n', 'photography\n', 'spotlight\n', 'warehouse']
with open('words.txt', 'w') as f:
    f.writelines(word)
print()

with open('words.txt', 'r') as f:
    count = 0
    words = f.readlines()
    for co in words:
        if len(co.strip('\n')) <= 10:
            count += 1

    print(count, '\n')


# >>> 27.6 심사 문제: 특정 문자가 들어있는 단어 찾기
with open('words1.txt', 'w') as F:
    F.write("Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.")

with open('words1.txt', 'r') as F:
    content = F.read()
    words = content.replace('.', '').replace(',', '').split()

    for i in words:
        if 'c' in i:
            print(i)

print()
# ===========================================================
# >>> CH.28
# ===========================================================

# >>> 28.1.1 반복문으로 문자 검사하기
word = input('단어를 입력하세요: ')

is_palindrome = True

for i in range(len(word) // 2):      
    if word[i] != word[-1 - i]:      
        is_palindrome = False        
        break

print(is_palindrome,'\n')                


# >>> 28.1.2 시퀀스 뒤집기로 문자 검사하기
word = input('단어를 입력하세요: ')
print(word == word[::-1],'\n') 


# >>> 28.1.3 리스트와 reversed 사용하기
word = 'level'
print(list(word) == list(reversed(word)),'\n')


# >>> 28.1.4  문자열의 join 메서드와 reversed 사용하기
word = 'level'
print(word == ''.join(reversed(word)),'\n')


# >>> 28.2.1  반복문으로 N-gram 출력하기
text = 'Hello'

for i in range(len(text) - 1):          
    print(text[i], text[i + 1], sep='')

print()


# >>> 28.2.2  zip으로 2-gram 만들기
text = 'hello'

two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')
print()


# >>> 28.2.3 zip과 리스트 표현식으로 N-gram 만들기
# text = 'hello'
print([text[i:] for i in range(3)],'\n')



# >>> 28.3 연습 문제: 단어 단위 N-gram 만들기
n = int(input())
text = input()
words = text.split()

if len(words) < n:
    print('worng')
else:
    n_gram = zip(*[words[i:] for i in range(n)]) 
    for i in n_gram:
        print(i)
print()


# >>> 28.4 심사 문제: 파일에서 회문인 단어 출력하기.
words = ['appche\n', 'decal\n', 'did\n', 'neep\n', 'noon\n', 'refer\n', 'river\n']
with open('words2.txt', 'w') as File:
    File.writelines(words)

with open('words2.txt', 'r') as File:
    content = File.read()
    words = content.split()

    for word in words:
        if word == word[::-1]:
            print(word)