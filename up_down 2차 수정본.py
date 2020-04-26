import random

users={}
userInfo=[]
best=10

def readFile(): #파일 내용을 읽어오는 함수
    f = open("ranking.txt" , 'r') #정보가 저장된 파일 오픈
    while True: #반복한다
        flines=(f.readlines()) #파일 내용을 flines리스트로 받는다
        if not flines:break #flines 없으면 while 탈출
        userInfo.append(flines) #userInfo리스트에 append한다
        
    for i in userInfo(): #foreach문 실행
        n,t=input(userInfo[i].split()) #공백으로 구분하여 n,t에 값을 넣는다
        users[n]=t #users딕셔너리에 값 넣는다.
    f.close()
        
def writeFile(best): #파일에 내용을 입력하는 함수
        name = str(input("\n닉네임을 입력하세요 >> ")) #사용자 닉네임 받기
        users[name]=best#users딕셔너리에 값 넣기
        sorted_users=sorted(userInfo.items(),key=lambda x:x[1]) #users안의 값을 sort한 값을 sorted_users에 저장
        print(sorted_users) #확인용 코드
        my_keys=list(sorted_users.keys()) #sorted_users키 값만 저장한 my_keys 리스트 생성
        f = open("ranking.txt" , 'w')
        for i in my_keys: #키 값 개수동안 반복
            f.write("%s  %d \n" %(i, sorted_users[i])) #파일에 정렬된 내용을 씀
            print('a') #확인용 코드
        f.close()

print("UP & DOWN 게임에 오신걸 환영합니다~")#게임 시작

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
                        break #탈출
                elif num > maxNum or num < miniNum: #num이 범위를 밖일 경우
                        print("\n범위를 초과하셨습니다. 다시 입력하여 주십시오") #오류 메세지 출력
                else: #그 외 값 입력시
                        if num > answer: #answer 보다num이 클 떄
                            maxNum = num-1 # 최대값 범위 변경
                            print("DOWN")
                        elif num < answer: #answer 보다num이 작을 때
                            miniNum = num+1 # 최소값 범위 변경
                            print("UP")
                        i+=1 #i카운트 함
    elif menu == 2: #메뉴가 2일 때 코드
        print("rank/name/score\n")
        k=1
        for i in userInfo:
            print("%d %s %d\n" %(k,i,users[i])) #딕셔너리 내용 출력
            k+=1 #랭킹 순위++
    elif menu == 3: #메뉴가 3일 때 코드
        break #종료
    else: # 그 외 값 입력 시
        print("다시 입력하여 주십시오") #오류 메세지 출력
