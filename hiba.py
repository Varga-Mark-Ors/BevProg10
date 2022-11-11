def main():

    try:
        d1=int(input("Szám pls="))
        d2=int(input("Szám pls="))
        print(d1/d2)
    #except ZeroDivisionError:
     #   print("0-val nem lehet More")
    except ZeroDivisionError:
        
        print(d1)
    except (ValueError):#,KeyboardInterrupt):
        #pass
        print("Ez nem szám tesókám")
    except KeyboardInterrupt:
        print("Keyboardnemjou")
    except:
        print("Imma head out") 
    print("Vege!")

if __name__=="__main__":
    main()