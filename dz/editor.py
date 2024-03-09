class editor():
    def __init__(self, a, c):
        self.a = a
        self.c = c
    def conslusion(self):
        dataRead = open("file.txt","r").read()
        print(dataRead)
    def change(self):
        dataWrite = open("file.txt","w")
        dataWrite.write(self.a)
        dataWrite.close()
    def add(self):
        dataAdd = open("file.txt","a")
        dataAdd.write(self.c)
        dataAdd.close()
b = editor(input(), input())
b.conslusion()
b.change()
b.add()