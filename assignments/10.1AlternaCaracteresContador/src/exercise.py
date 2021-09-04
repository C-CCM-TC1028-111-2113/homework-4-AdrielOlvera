def main():
    #escribe tu código abajo de esta línea
x=+int(input())
for(i) in range(x):
    if ((i+1)%2)==0:
        print(str(i+1)+"-%")
    elif ((i+1)%2)!=0:
        print(str(i+1)+"-#")
        

    pass

if __name__=='__main__':   
    main()
