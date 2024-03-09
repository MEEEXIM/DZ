class meneger():
    def __init__(self, a, b):
        self.a = str(a)
        self.b = str(b)
    def new(self):
        with open("file.txt",'r') as file:
            fileRead = file.readlines()
            fileARR = []
            c=0
            for i in fileRead:
                c+=1
                if c % 2 == 1:
                    if i == self.a:
                        return self.a
                fileARR.append(i)
            fileARR.append(self.a)
            fileARR.append(self.b)
            fileRead = fileARR
    def del(self):
    
a=meneger('asd', '555')
a.new()




class meneger():
    def __init__(self, a, b):
        self.a = str(a)
        self.b = str(b)
    def new(self):
        with open("file.txt",'r') as file:
            fileRead = file.readlines()
            fileARR = []
            
                fileARR.append(i)
            fileARR.append(self.a)
            fileARR.append(self.b)
            fileRead = fileARR
    def dell(self):
    
a = ''
while a != 'ex' or a != 'exit':
    a = input()
    
    if a = 'new':


          
