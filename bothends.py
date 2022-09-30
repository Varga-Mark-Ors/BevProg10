def bothend(sy):
    
    if len(sy)<2:
        return ""
    else:
        d=len(sy)
        be=sy[0:2]
        ki=sy[d-2:d]
        return be+ki

def main():
    szo=input("Szo:")
    #szo="Ronaldo"
    both=bothend(szo)
    print(both)
if __name__=="__main__":
    main()