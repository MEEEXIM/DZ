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
car1 = cars('Russia', '1st', 1999, 130)
car2 = cars('USA', '2nd', 2015, 160)
car3 = cars('Russia', '2nd', 2021, 250)
b = int(input('Какой  автомобиль?'))
a = int(input('Какое растояние?'))
if b == 1:
    car1.info()
    car1.T(a)
elif b == 2:
    car2.info()
    car2.T(a)
else:
    car3.info()
    car3.T(a)