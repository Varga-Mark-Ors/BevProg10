def main():
    natrium= int(input("Natrium: "))
    chloride= int(input("Chloride: "))
    nacl=0
    excessNA=0
    excessCL=0

    if natrium==chloride*2:
        nacl=chloride*2
    elif natrium>chloride*2:
        nacl=chloride*2
        excessNA=(natrium-chloride*2)*2
    else:
        nacl=natrium
        excessCL=chloride*2-natrium
    print('Letrejott so:{0},maradek natrium:{1},maradek klor:{2}' .format(nacl,excessNA,excessCL))

if __name__=="__main__":
    main()