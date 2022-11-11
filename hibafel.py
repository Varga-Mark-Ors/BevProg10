def main():
   
    while True:
        try:
            szam1=float(input("1.szam="))
            szam2=float(input("2.szam="))
            result=szam1/szam2
            print('Az osztas eredmenye:{0:.2f}'.format(result))
            print("-"*10)
        except (ValueError):
            print("Unfortunately this is not a number, try again!")
        except KeyboardInterrupt:
            break
        except ZeroDivisionError:
            print("Unfortunately you cannot divide with 0, try again!")    
######
if __name__=="__main__":
    main()