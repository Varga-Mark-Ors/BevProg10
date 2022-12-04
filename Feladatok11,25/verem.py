class Verem():
    def __init__(self,kov=[]) -> None:
        self.kov=kov

    def ures(self):
        if len(self.kov)==0:
            return True
        else:
            return False

    def betesz(self,x):
        self.kov.append(x)

    def kivesz(self):
        if len(self.kov)==0:
            print("A vektor ures, nem lehet kivenni")
        else:
            x=self.kov.pop()
            print(x)
    def __str__(self):
        return "({})".format(self.kov)

    def __repr__(self) -> str:
        return "({})".format(self.kov)


def main():
    v=Verem()
    i=1
    while i!=0:
        i=int(input(('Mit csinalunk?(Press 1 for help)=')))
        if i==1:
            print('1-Help,2-Üres-e,3-Betesz,4-Kivesz,5-Kiír,0-Exit')
        elif i==2:
            print(v.ures())
        elif i==3:
            j=int(input(('Milyen szamot tegyunk be?=')))
            v.betesz(j)
        elif i==4:
            v.kivesz()       
        elif i==5:
            print(v)
        elif i==0:
            break
        else:
            print('Nem jo szamot adot meg!!!')

if __name__=="__main__":
    main()