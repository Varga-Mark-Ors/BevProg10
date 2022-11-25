import random

def main():
    a=random.randint(1,100)
    #print(a)
    min=1
    max=100
    kindex=int(input('Tipp:'))
    #print(kindex)
    while kindex!=a :
        if kindex>a :
            print("My number is smaller, than", kindex)
            kindex=int(input('Tipp: '))
        elif kindex<a :
            print("My number is bigger, than",kindex)
            kindex=int(input('Tipp: '))
    print("You guessed it,it was",kindex)
if __name__=="__main__":
    main()