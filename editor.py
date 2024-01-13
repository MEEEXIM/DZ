class editor():
    def __init__(self, a):
        self.a = a
    def conslusion(self):
        dataRead = open("file.txt","r").read()
        print(dataRead)
        dataRead.close()
    def change(self):
        dataWrite = open("file.txt","w")
        dataWrite.write(self.a)
        dataWrite.close()
    def add(self):
        dataAdd = open("file.txt","a")
        dataAdd.add(self.a)
        dataAdd.close()
b = editor(input())
b.conslusion()
b.change()