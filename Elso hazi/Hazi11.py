def main():
    age =int(input('Age: '))

    if age>=21:print('Fogyaszthat alkoholt USA-be')
    else:print('Nem fogyaszthat alkoholt USA-be')

    if age>=18 :print('Vasarolhat cigarettat Magyarorszagon')
    else:print('Nem vasarolhat cigarettat Magyarorszagon')

    if age>=16 :print('Szerezhet jogositvanyt')
    else:print('Nem szerezhet jogositvanyt')

    if age>=7:print("Megnezheti a Shrek 2-t")
    else:print("Nem nezheti meg a Shrek 2-t")
if __name__=="__main__":
    main()