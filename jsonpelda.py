import json

def main():
    f=open("easy.json",'r')
    d=json.load(f)
    print(d)
    print(type(d))
    print('-'*10)
    print(d['first'])
    print(type(d['first']))
    print('-'*10)
    f.close()
if __name__=="__main__":
    main()