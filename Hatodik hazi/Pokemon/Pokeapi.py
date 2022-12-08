import json

def main():
    
    f = open('jokeson.json','w') 
    nev=input('Pokemon neve?=')
    ev=int(input('Eletkora?='))
    mag=int(input('Magassaga?(cm)='))
    suly=int(input('Sulya?(kg)='))
    d={
            'neve':nev,
            'eletkor':ev,
            'magas':mag,
            'tomeg':suly,
    }
    json.dump(d,f,indent=3)

if __name__ == "__main__":
    main()