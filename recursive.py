# 재귀 함수 호출
# for i in range(1,6):
#     print(i)
#     if i == 5:
#         print("번호 끝")

def count_1(): #첫번째 군인
    print(1)
    count_2()
    print("1끝")

def count_2(): #두번째 군인
    print(2)
    count_3()
    print("2끝")

def count_3(): #세번째 군인
    print(3)
    count_4()
    print("3끝")

def count_4(): #네번째 군인
    print(4)
    count_5()
    print("4끝")

def count_5(): #다섯번째 군인
    print(5)
    print("번호끝")
    print("5끝")

# count_1()

def count(num):
    if(num < 100):
        print(num)
        count(num +1)

count(1)