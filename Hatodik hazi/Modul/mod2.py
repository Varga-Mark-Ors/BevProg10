import modult as m

def main():
    #b=199
    b=int(input("Meddig nezuk?="))
    i=2
    ossz=0

    while i<=b:
        if m.is_prime(i)==True:
            ossz=ossz+i       
        i=i+1

    print("Primek osszege=",ossz)    
if __name__ == "__main__":
    main()