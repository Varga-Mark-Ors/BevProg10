import json

def main():
    f=open("jokeson.json",'r')
    d=json.load(f)
    i=1
    while i!=0:
        i=int(input(('Mit csinalunk?(Press 1 for help)=')))
        if i==1:
            print('1-Help,2-Kiir mindent,3-Kiirja a nevet,4-Kiirja a eletkorat,5-Kiirja a magassagat,6-Kiirja a sulyat,0-Exit')
        elif i==2:
            print(d)
        elif i==3:
            print(d['neve'])
        elif i==4:
            print(d['eletkor'],'eves')     
        elif i==5:
            print(d['magas'],'cm')
        elif i==6:
            print(d['tomeg'],'kg')
        elif i==0:
            break
        else:
            print('Nem jo szamot adot meg!!!')
if __name__ == "__main__":
    main()