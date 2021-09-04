
def main():
    #escribe tu código abajo de esta línea
index=int(input("Enter the index: "))
x=1
s=1
y=1
while s!=index:

    a=x+y
    x=y
    y=a
    s=s+1
print(str(x))

    pass

if __name__=='__main__':
    main()
