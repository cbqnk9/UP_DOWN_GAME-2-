l1=[1,2,3]
l2=['a','b','c',l1]

l3=l1*2 #l3는 l1을 반복한 리스트

print(str(l1[2])+"hi"+"\n") #3hi 출력되는 것, l1의 안의 값이 바뀌는 것은 아님
print(l1 ,l2)


l1.append('a') #맨 마지막에 요소 추가함, 타입 상관x
print(l1)

del l1[2] #요소 제거해줌
print(l1)

l1.remove(2) #제일 처음 나오는 ()값 제거해줌, ()값 없을 땐 에러발생
print(l1)

l1.insert(1,2) #(a,b) a번째에 b값 추가
print(l1)

l3.reverse() #함수 순서를 뒤집어 준다
print(l3)

l3.sort() #정렬함수
print(l3)

print(l3.pop(2)) #리스트 ()번째 요소 리턴하고 삭제
print(l3)

print(l3.count(1)) #리스트 안 ()갯수 리턴
