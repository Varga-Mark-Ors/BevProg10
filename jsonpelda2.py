import json

def main():
    f=open("pelda.json",'r')
    f2=open("pelda.txt",'w')
    d=json.load(f)
    print(d)
    print(type(d))
    print()
   #  print('-'*10)
    print(d['people'][0]['name'])
    print()
    print(type(d['people'][0]['name']))
    jsontxt=json.dumps(d)
    print(jsontxt,file=f2)
    f.close()
if __name__=="__main__":
    main()