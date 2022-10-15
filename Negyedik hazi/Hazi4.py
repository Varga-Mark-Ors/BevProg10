class Progceg():
    def __init__(self,nev,fizetes,rang='Junior',dolgev=0) -> None:
        self.nev=nev
        self.fizetes=fizetes
        self.rang=rang
        self.dolgev=dolgev
        
    
    def emel(self,x):
        if x>0:
            self.fizetes=self.fizetes+x
        else:
            self.fizetes+=10000
        print(self.fizetes)

    def evek(self,a):
        self.dolgev=a+1
        print(self.dolgev)

    def rangok(self,b):
        if self.dolgev<1:
            self.rang='Intern'
        elif self.dolgev<3:
            self.rang='Junior'
        elif self.dolgev<6:
            self.rang='Medior'
        else:
            self.rang='Senior'
        print(self.rang)

    def __str__(self):
        return "{}:{};{};{}".format(self.nev,self.fizetes,self.rang,self.dolgev)

def main():
    db=int(input("Hany ember lesz?"))
    i=0
    x=[]
    while i<db:
        a=input('Nev?')
        b=int(input('Fizetes?'))
        c=input('Rang?')
        d=int(input('Evek ledolgozva?'))
        x.append(i)
        f=Progceg(a,b,c,d)
        x[i]=f
        i=i+1

    i=0
    while i < db:
        a=int(input('Mennyit emel?'))
        x[i].emel(a)
        i=i+1

    i=0
    while i < db:
        x[i].evek(x[i].dolgev)
        i=i+1

    i=0
    while i < db:
        x[i].rangok(x[i].dolgev)
        i=i+1

    i=0
    while i < db:
        print(x[i])
        i=i+1
if __name__ == '__main__':
    main()