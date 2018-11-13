# class Students:
#     name="gokul"
#     rollno=11
#     def getage(self,myage):
#         print('age is'+str(myage))
# s=Students()
# x=int(input("enter the age"))
# print(s.getage(x))        


# class Students:
#   def __init__(self,x,y):
#         self.name=x
#         self.rollno=y
    
#   def printdata(self):
#         print("Name=",self.name)
#         print("Rollno=",self.rollno)
#   def getage(self,myage):
#         print('age is'+str(myage))
# s=Students("gokul",11)
# x=int(input("enter the age"))
# s.printdata()
# s.getage(x)        


class Employe:
   def __init__(self,a,b,c,d):
        self.name=a
        self.emcode=b
        self.salary=c
        self.age=d

   def printdata(self):
       print("Name=",self.name)
       print("emcode=",self.emcode)
       print("salary=",self.salary)
       print("age=",self.age)
x=Employe("gokul","rty",2500,21)
y=Employe("akhil","pqr",2501,22)
z=Employe("vishnu","mno",2502,20)
p=Employe("arya","qwe",2504,19)
x.printdata()
y.printdata()
z.printdata()
p.printdata()
       
