#1. 윤년 구하기
year = int(input("연도를 입력하세요 : "))

if (year % 4 == 0):
    if (year % 100 != 0 or year % 400 == 0):
        print(1)
    else : 
        print(0)
else:
    print(0)


#2. 자연수 N 출력하기
num = int(input("자연수 N을 입력하세요 : "))
for i in range(0, num):
    print(num-i)

'''
a = int(input())

for i in range(a, 0, -1):
		print(i)

# range범위에 reversed 함수를 씌워서 역 순으로 출력하게 생산 가능. 
a = int(input())
for i in reversed(range(a)):
    print(i+1)
'''
#3. 정수 계산기
while (True):
    try :
        num1 = int(input("정수 A를 입력하세요 : "))
        num2 = int(input("정수 B를 입력하세요 : "))
        total = num1 + num2
        print(total)
    except : 
        print("정수가 아닙니다!")
        break

'''
✔️ 한 가지 힌트 더. map 함수 알려드립니다. 일일이 레인지 함수로 처리하지 

map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다
(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).

try - except 구문의 기본적인 구조는 try 구문➡️ 에러가 발생할 가능성이 있는 코드를 작성하고 except 구문  ➡️ 예외 발생 시 실행할 코드를 작성하는 것이다.
이 구문을 사용하는 이유는, 에러를 발생해도 프로그램을 멈추지 않고 작동시키기 위해서 입니다.
사용자가 A, B에 정수만 넣어야하는 것을 깜빡한다면 에러가 발생할 수 있기 때문입니다.
*try-except 와 while 배치를 고려해봅시다.

try:
		while True:
        A, B = map(int, input().split())
        print(A+B)
except:
        break

3번 문제 정답
while과 try의 순서를 바꾸어도 잘 된다고 한다.
'''
