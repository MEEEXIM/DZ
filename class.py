class cars:
    def __init__(self, proizv, model, god, V):
        self.proizv = proizv
        self.model = model
        self.god = god
        self.V = V
    def info(self):
        print(self.proizv, self.model, self.god, self.V)
    def T(self, a):
        c=a/self.V
        print(c)
car1 = cars('Russia', '1stmodel', 1999, 130)
car2 = cars('USA', '2nd model', 2015, 160)
car3 = cars('Russia', '2ndmodel', 2021, 250)
# b = int(input('Какой  автомобиль?'))
# a = int(input('Какое растояние?'))
# if b == 1:
#     car1.info()
#     car1.T(a)
# elif b == 2:
#     car2.info()
#     car2.T(a)
# else:
#     car3.info()
#     car3.T(a)








# номер 1
class calcul:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def delenie(self):
        print(self.a / self.b)
    def umnogenie(self):
        print(self.a * self.b)
    def vichitanie(self):
        print(self.a - self.b)
    def slogenie(self):
        print(self.a + self.b)
c=''
while c != '==':
    c=input()
    f=calcul(int(input()), int(input()))
    if c == '/':
        f.delenie()
    elif c == '*':
        f.umnogenie()
    elif c == '-':
        f.vichitanie()
    else:
        f.slogenie()