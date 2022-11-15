def main():
    f=open("Barmi1.txt", 'w')
    d=open("Barmi1.txt", 'a')
    a=input('Szoveg=')
    while a!='':
        print(a, file = d)
        a=input('Szoveg=')
    d.close()
    f.close()
if __name__ == "__main__":
    main()