import random

users=[]
flines=[]
best=11

def readFile(): #파일 내용을 읽어오는 함수
    global users
    global flines
    f = open("ranking.txt" , 'r') #정보가 저장된 파일 오픈
    while True: #반복한다
        users=(f.readlines()) #파일 내용을 flines리스트로 받는다
        if not flines:break #flines 없으면 while 탈출    
    f.close()
        
def writeFile(best): #파일에 내용을 입력하는 함수
    global users
    global flines
    name = str(input("\n닉네임을 입력하세요 >> ")) #사용자 닉네임 받기
    users.append("%d    %s\n" %(best,name)) #리스트에 추가
    users.sort() #리스트 정렬
    if users[0][:2] == str(10): #최고기록이 10일 때 값 맨 뒤로 보낸다
        l=users[0]
        del users[0]
        users.append(l)
        
    f = open("ranking.txt" , 'w')
    for i in users: 
        f.write(i) #파일에 정렬한 users값 넣는다
    f.close()

def renewBest(): #best값 갱신하는 함수 생성
    global best
    f=open("ranking.txt",'r')
    times=(f.readline())
    f.close()
    if (times): #times에 값이 있을 때
        best=int(times[:2]) #파일의 첫번째 값을 best로 받는다.(문자열로 입력받으니 형변환 해준다)

renewBest()
print("UP & DOWN 게임에 오신걸 환영합니다~")#게임 시작
readFile()
while True: #계속 반복한다
    print("\n1. 게임시작 2. 기록확인 3. 게임종료") #메뉴 안내
    menu = int(input(">>")) #메뉴값을 입력받음
    if menu == 1: #메뉴가 1일 때 코드
        answer = random.randint(1,100) #랜덤 난수 answer생성 (범위는 1~100)
        maxNum = 100 #범위 최대값 100 초기화
        miniNum = 1 #범위 최소값 1 초기화
        i=1 # i값 초기화
        print(answer) #답 확인용 코드
        while i < 11: #i가 11보다 작을 때까지 반복
                num = int(input("%d번째 숫자 입력(%d~%d)" %(i,miniNum,maxNum))) #예상값 num입력받음
                if num == answer: #num 과answer이 값을 경우
                        print("\n정답입니다!!\n%d번째만에 맞추셨습니다" %(i)) #맞춘 횟수 안내
                        if best > i: #최고기록보다 적으면
                            best = i #최고 기록 변경
                            readFile() #파일 내용 읽어 딕셔너리 저장
                            writeFile(best) # 새로운 기록 저장
                            renewBest() #best값 갱신
                        break #탈출
                elif num > maxNum or num < miniNum: #num이 범위를 밖일 경우
                        print("\n범위를 초과하셨습니다. 다시 입력하여 주십시오") #오류 메세지 출력
                else: #그 외 값 입력시
                        if num > answer: #answer 보다num이 클 때
                            maxNum = num-1 # 최대값 범위 변경
                            print("DOWN")
                        elif num < answer: #answer 보다num이 작을 때
                            miniNum = num+1 # 최소값 범위 변경
                            print("UP")
                        if i==10:
                            print("입력횟수를 초과하였습니다. 게임오버!")#입력횟수 초과시 출력
                        i+=1 #i카운트 함
    elif menu == 2: #메뉴가 2일 때 코드
        k=1
        print("rank/score/name")
        for i in users:
            print("%d    %s"%(k,i)) #순위와 파일 내용을 출
            k+=1 #랭킹 순위++
    elif menu == 3: #메뉴가 3일 때 코드
        break #종료
    else: # 그 외 값 입력 시
        print("다시 입력하여 주십시오") #오류 메세지 출력
