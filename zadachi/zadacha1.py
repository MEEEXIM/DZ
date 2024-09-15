K=int(input())
N=int(input())
a=1
f=0
a1=0
b1=0
b=N-a
while f!=K:
    if b==1:
        a=1
        b=N-a
    a1+=a
    b1=b1+N-a
    b=N-a
    a+=1
    f+=1
if a1>b1:
    print('Pit '+str(a1-b1))
elif b1>a1:
    print('Vas '+str(b1-a1))
else:
    print(0)
#выдает неверный ответ