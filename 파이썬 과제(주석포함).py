import random

rank=1
best=10

def correct(rank,result):
        userInfo = str(input("\n닉네임을 입력하세요 >> "))
        f = open("ranking.txt" , 'a')
        f.write("%d  %s  %d" %(rank, userInfo, result))
        f.close()

print("UP & DOWN 게임에 오신걸 환영합니다~")

while True:
    print("\n1. 게임시작 2. 기록확인 3. 게임종료")
    menu = int(input(">>"))
    if menu == 1:
        num = random.randint(1,100)
        maxNum = 100
        miniNum = 1
        i=1
        while i < 11:
            expectNum = int(input("%d번째 숫자 입력(%d~%d)" %(i,miniNum,maxNum)))
            i+=1
            if num == expectNum:
                print("\n정답입니다!!\n%d번째만에 맞추셨습니다" %(i))
                result=i
                if best > result:
                    best = result
                    correct(rank,result)
                    rank =+ 1 #피드백 1,4번 수정
                break
            elif expectNum > maxNum or expectNum < miniNum:
                i-=1
                print("\n범위를 초과하셨습니다. 다시 입력하여 주십시오")
                #피드백 2,3번 수정
            else:
                if expectNum > num:
                    maxNum = expectNum-1
                    print("DOWN")
                elif expectNum < num:
                    miniNum = expectNum+1
                    print("UP")
    elif menu == 2:
        f = open("ranking.txt", 'r')
        data = f.read()
        print("\n%s" %data)
        f.close()
    elif menu == 3:
        break
    else:
        print("다시 입력하여 주십시오")
