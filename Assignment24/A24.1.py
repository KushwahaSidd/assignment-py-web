
class Students:

    def __init__(self,name,age,email):
            self.name=name
            self.age=age
            self.email=email
    def show(self):
        print(self.name , self.age , self.email, sep="\n")

obj=Students("siddharth",21,"sidhgzp0548@gmail.com")       
obj.show()