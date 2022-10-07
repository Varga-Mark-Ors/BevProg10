
class BankSzamla():

    def __init__(self, nev, egyenleg)->None:
            self.nev=nev
            self.egyenleg=egyenleg
            self.dupont=1000

    def betesz(self,osszeg):
        self.egyenleg+=osszeg
    
    def kivesz(self,osszeg):
        if self.egyenleg<osszeg:
            print("Csoro vagy testvirem!!!")
        else:
            self.egyenleg-=osszeg

    def kiir(self):
        print("Tulaj:{0},egyenleg:{1}".format(self.nev,self.egyenleg))
def main():
    b1=BankSzamla("Dani",600)
    b1.kivesz(1000)
    b1.betesz(200000)
    b1.kivesz(1000)
    b1.kiir()
if __name__=="__main__":
    main()