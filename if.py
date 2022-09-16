def main():
    age =int(input('Age: '))

    if age >= 18: 
        print('Igen')
    elif age == 17:
        print('Majdnem')
    else:
        print('Nem')
if __name__=="__main__":
    main()