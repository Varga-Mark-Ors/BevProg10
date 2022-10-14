from cmath import *

class Point():
    #private,protected,public osztalyok
    def __init__(self,x=0,y=0) -> None:
        self.x=x
        self.y=y

    def dist(self,x,y):
        return sqrt((self.x-x)**2+(self.y-y)**2)

    def dis(self,z):#:'Point'):
        return sqrt((self.x-z.x)**2+(self.y-z.y)**2)
    
    def __str__(self):
        return "({};{})".format(self.x,self.y)

    def __repr__(self)->str:
        return "({};{})".format(self.x,self.y)

def FirstQuarter(li):
    return [p for p in li if (p.x > 0 and p.y> 0)]

def main():
    a=Point(3,4)
    b=Point(-2,5)
    c=Point(-7,-2) 
    print(a)
    print(a.dist(3,2))
    print(a.dis(b))
    print(FirstQuarter([a,b,c]))
if __name__=="__main__":
    main()