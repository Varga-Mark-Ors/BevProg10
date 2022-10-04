def Cesar(a,b):
    text=""
    for c in a:
     for d in b:
      if c==d :
        text=text+c
    return text

def main():
    text=(input('Text: '))
    #text="kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    texte=Cesar(text,chars)
    print(texte)
if __name__=="__main__":
    main()