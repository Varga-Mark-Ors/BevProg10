from enum import Enum


class Type(Enum):
    House='House'
    BOF='Block of Flats'
    tree='Treeeeeeeeeee'
    Free='Szabad'



class Place:
    def __init__(self,begin,end) -> None:
        self.begin=min(begin,end)
        self.end=max(begin,end)
        self.type=Type.Free
    
    def distance(self) -> float :#float
        return self.end-self.begin
    
    def __str__(self) -> str:
        return '({0},{1})'.format (self.begin,self.end)
    
    def __add__(self,b): #self + b
        newelement=Place(min(self.begin,b.begin),max(self.end,b.end))
        return newelement

    def __sub__(self,b): #self -b 
        newelement=Place(max(self.begin,b.begin),min(self.end,b.end))
        return newelement
    
    def __ge__(self,b): #greater than,equal self>=b
        if self.distance() >= b.distance():
            return True
        else:
            return False

#__gt__ greater than, __lt__ less than, __le__less equal, __eq__ equal,
#  __ne__ not equal

    def __iadd__(self,b): #self+=b
        newelement=Place(min(self.begin,b.begin),max(self.end,b.end))
        return newelement

    

def main():
    print(Type.BOF.value)
    print(Type.BOF.name)
    a=Place(4,6)
    b=Place(2,9)
    print(a.distance())
    print(a+b)
    print(a-b)
    #print(a+=b)
    print(a>=b)
    #print(a)
if __name__=="__main__":
    main()