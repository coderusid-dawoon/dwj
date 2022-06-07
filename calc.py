from turtle import goto


print("계산기")

def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y

while True:
    print("\n사칙연산을 선택하세요\n")
    print("1번 더하기")
    print("2번 빼기")
    print("3번 곱하기")
    print("4번 나누기")
    print("\n0번 종료\n")

    choice = int(input())

    if choice == 0:
        print("\n계산기를 종료합니다.")
        break

    num1 = int(input("첫번째 숫자를 입력하세요\n"))
    num2 = int(input("두번째 숫자를 입력하세요\n"))

#while True:
    if choice == 1:
        print(str(num1) +' + '+ str(num2) + ' = ' + str(add(num1, num2)))

    elif choice == 2:
        print(str(num1) +' - '+ str(num2) + ' = ' + str(subtract(num1, num2)))

    elif choice == 3:
        print(str(num1) +' * '+ str(num2) + ' = ' + str(multiply(num1, num2)))

    elif choice == 4:
        print(str(num1) +' / '+ str(num2) + ' = ' + str(divide(num1, num2)))

    else : 
        print("알맞은 숫자를 다시 입력하세요")